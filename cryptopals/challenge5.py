#!/usr/bin/env python
#
# I was thrown off on this one by the random line break in the "correct" output.
# The two lines of input do not correspond to the two lines of output.
# For the first time, we're expected to handle the newline.

import sys
import itertools
from cryptopals.challenge2 import bits_to_hex

def str_to_bits(s):
    bits = []
    for ch in s:
        x = ord(ch)
        bits.append(1 if x & 0b10000000 else 0)
        bits.append(1 if x & 0b01000000 else 0)
        bits.append(1 if x & 0b00100000 else 0)
        bits.append(1 if x & 0b00010000 else 0)
        bits.append(1 if x & 0b00001000 else 0)
        bits.append(1 if x & 0b00000100 else 0)
        bits.append(1 if x & 0b00000010 else 0)
        bits.append(1 if x & 0b00000001 else 0)
    return bits


def repeating_xor(bits, cipher):
    return [
        1 if b1 != b2 else 0
        for b1, b2 in zip(bits, itertools.cycle(cipher))
    ]


if __name__ == '__main__':
    code, filename = sys.argv[1:]
    # lines = [line.strip() for line in open(filename).readlines()]
    data = open(filename).read()

    # print(f'{line=}')
    bits = str_to_bits(data)
    # print(bits)
    cipher = str_to_bits(code)
    bits = repeating_xor(bits, cipher)
    print(bits_to_hex(bits))
