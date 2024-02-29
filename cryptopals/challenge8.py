#!/usr/bin/env python
# https://github.com/ricpacca/cryptopals/ uses PyCrypto,
# but that's deprecated. I used cryptography.

import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptopals.challenge2 import hex_to_bits
from cryptopals.challenge3 import bits_to_bytes


if __name__ == '__main__':
    lines = [line.strip() for line in open(sys.argv[1]).readlines()]
    key = b"YELLOW SUBMARINE"
    assert len(key) == 16  # 128 bits

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    for line in lines:
        bits = hex_to_bits(line)
        in_bytes = bytes(bits_to_bytes(bits))

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(in_bytes) + decryptor.finalize()

        print(plaintext)
