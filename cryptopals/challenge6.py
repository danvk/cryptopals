#!/usr/bin/env python

import sys


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


if __name__ == '__main__':
    bits = [
        bit
        for line in open(sys.argv[1]).readlines()
        for bit in base64_to_bits(line.strip())
    ]
    print(len(bits))
