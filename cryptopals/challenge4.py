#!/usr/bin/env python
#
# I got quite stuck on this one because I counted "space" as an invalid character.

import fileinput
from cryptopals.challenge2 import hex_to_bits

from cryptopals.challenge3 import find_best_single_xor


# def str_to_bits(s):
#     bits = []
#     for ch in s:
#         x = ord(ch)
#         bits.append(1 if x & 0b10000000 else 0)
#         bits.append(1 if x & 0b01000000 else 0)
#         bits.append(1 if x & 0b00100000 else 0)
#         bits.append(1 if x & 0b00010000 else 0)
#         bits.append(1 if x & 0b00001000 else 0)
#         bits.append(1 if x & 0b00000100 else 0)
#         bits.append(1 if x & 0b00000010 else 0)
#         bits.append(1 if x & 0b00000001 else 0)
#     return bits


if __name__ == '__main__':
    candidates = []
    for line in fileinput.input():
        s = line.strip()
        while len(s) < 60:
            s = '0' + s
        assert len(s) == 60, f'{s=}'
        bits = hex_to_bits(s)
        assert len(bits) == 240
        c = find_best_single_xor(bits)
        if c:
            print(c)
            candidates.append(c)

    print(min(candidates))
