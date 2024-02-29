#!/usr/bin/env python

import sys

from cryptopals.challenge3 import bits_to_bytes


def edit_distance(bits1, bits2):
    assert len(bits1) == len(bits2)
    return sum(
        1 if b1 != b2 else 0
        for b1, b2 in zip(bits1, bits2)
    )


def base64_to_num(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return 26 + ord(c) - ord('a')
    elif '0' <= c <= '9':
        return 52 + ord(c) - ord('0')
    elif c == '+':
        return 62
    elif c == '/':
        return 63
    elif c == '=':
        return 0  # ???
    raise ValueError(c)


def base64_to_bits(str):
    bits = []
    for c in str:
        num = base64_to_num(c)
        bits.append(1 if num & 0b100000 else 0)
        bits.append(1 if num & 0b010000 else 0)
        bits.append(1 if num & 0b001000 else 0)
        bits.append(1 if num & 0b000100 else 0)
        bits.append(1 if num & 0b000010 else 0)
        bits.append(1 if num & 0b000001 else 0)
    return bits


def chunk(xs: list, n: int):
    # split an array into chunks of length n; may truncate last one
    for i in range(0, len(xs), n):
        if i + n > len(xs):
            break
        yield xs[i:i+n]


if __name__ == '__main__':
    bits = [
        bit
        for line in open(sys.argv[1]).readlines()
        for bit in base64_to_bits(line.strip())
    ]
    print(len(bits), 'bits')

    # best keysizes:
    # 5: (1.2, ks=5, ed=6)
    # 3: (2.0, ks=3, ed=6)
    # 2: (2.5, ks=2, ed=5)
    scores = []
    for keysize in range(2, 41):
        keysize_bits = 8 * keysize
        first = bits[0:keysize_bits]
        second = bits[keysize_bits:2*keysize_bits]
        assert len(first) == keysize_bits
        assert len(second) == keysize_bits
        distance = edit_distance(first, second)
        norm_d = distance / keysize
        scores.append((norm_d, keysize, distance))
    scores.sort()
    print(scores[:3])
    keysize = scores[0][1]
    print(f'{keysize=}')

    u8s = bits_to_bytes(bits)
    blocks = [*chunk(u8s, keysize)]
    print(f'n blocks: {len(blocks)}')
    print(len(blocks[0]))
    print(len(blocks[-1]))

    trans = [*zip(*blocks)]
    print(f'n trans={len(trans)}')
    print(f'n trans[0]={len(trans[0])}')
