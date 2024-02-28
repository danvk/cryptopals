#!/usr/bin/env python
# Single-byte XOR cipher
# Cooking MC's like a pound of bacon

import sys

from cryptopals.challenge2 import hex_to_bits, HEX_DIGITS, xor


def bits_to_bytes(bits):
    out = []
    acc = 0
    for i, bit in enumerate(bits):
        acc *= 2
        if bit:
            acc += 1
        if i % 8 == 7:
            out.append(acc)
            acc = 0
    return out


def bytes_to_ascii(bs):
    return ''.join(chr(b) for b in bs)


def is_ascii(bytes):
    for b in bytes:
        if b >= 128 or b < 32:
            return False
    return True


SCRABBLE = [
    (1, 'AEIOULNSTR'),
    (2, 'DG'),
    (3, 'BCMP'),
    (4, 'FHVWY'),
    (5, 'K'),
    (8, 'JX'),
    (10, 'QZ'),
]

def score_letter(ch: str):
    ch = ch.upper()
    for pts, chars in SCRABBLE:
        if ch in chars:
            return pts
    return 99


def score_phrase(letters: str):
    return sum(score_letter(ch) for ch in letters)


def find_best_single_xor(bits):
    assert len(bits) % 8 == 0

    scores = []

    for h1 in HEX_DIGITS:
        bits1 = hex_to_bits(h1)
        for h2 in HEX_DIGITS:
            bits2 = hex_to_bits(h2)
            bits_cipher = bits1 + bits2
            assert len(bits_cipher) == 8
            bits_cipher *= (len(bits) // 8)
            out = xor(bits, bits_cipher)
            u8s = bits_to_bytes(out)

            # if is_ascii(u8s):
            letters = bytes_to_ascii(u8s)
            # print(letters)
            scores.append((score_phrase(letters), h1+h2, letters))

    return min(scores) if scores else None


if __name__ == '__main__':
    (hex,) = sys.argv[1:]
    bits = hex_to_bits(hex)
    print(find_best_single_xor(bits))
