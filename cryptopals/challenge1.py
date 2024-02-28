#!/usr/bin/env python
# https://cryptopals.com/sets/1/challenges/1
# hex to base64

import fileinput


def base64(n: int):
    if n <= 25:
        return chr(ord('A') + n)
    elif n <= 51:
        return chr(ord('a') + (n - 26))
    elif n <= 61:
        return chr(ord('0') + (n - 52))
    elif n == 62:
        return '+'
    elif n == 63:
        return '/'
    raise ValueError(n)


def hex_to_base64(line):
    # Insight: 3 hex chars = 2 base64 chars
    # 3 * 4 = 2 * 6
    nbits = 0
    acc = 0
    out = []

    for char in line:
        acc *= 16
        acc += int(char, base=16)
        nbits += 4
        if nbits >= 6:
            if nbits == 6:
                char64 = acc
                acc = 0
            elif nbits == 8:
                char64 = acc >> 2
                acc = acc & 3
            else:
                raise ValueError(nbits)
            out.append(base64(char64))
            nbits -= 6

    if acc:
        assert acc < 64
        char64 = acc % 64
        out.append(base64(char64))

    return ''.join(out)


for line in fileinput.input():
    line = line.strip()
    print(hex_to_base64(line))
