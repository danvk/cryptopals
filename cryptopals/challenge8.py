#!/usr/bin/env python

# In this file are a bunch of hex-encoded ciphertexts.
# One of them has been encrypted with ECB.
# Detect it.
# Remember that the problem with ECB is that it is stateless and deterministic;
# the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

# Idea: look for repeated 16-byte chunks
# This works and produces a unique result… but are we supposed to decrypt the message?

import sys
from collections import Counter

from cryptopals.challenge2 import hex_to_bits
from cryptopals.challenge3 import bits_to_bytes
from cryptopals.challenge6 import chunk


if __name__ == '__main__':
    lines = [line.strip() for line in open(sys.argv[1]).readlines()]
    # key = b"YELLOW SUBMARINE"
    # assert len(key) == 16  # 128 bits

    #
    for i, line in enumerate(lines):
        bits = hex_to_bits(line)
        in_bytes = bytes(bits_to_bytes(bits))
        chunks = chunk(in_bytes, 16)
        counts = Counter(chunks)
        if counts.most_common(1)[0][1] > 1:
            print(counts.most_common(1))
            print(i, line)
