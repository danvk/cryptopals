#!/usr/bin/env python

import base64
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


if __name__ == '__main__':
    in_bytes = base64.decodebytes(open(sys.argv[1], 'rb').read())
    key = b"YELLOW SUBMARINE"
    assert len(key) == 16  # 128 bits
    # https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.Cipher
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(in_bytes) + decryptor.finalize()

    print(plaintext.decode())
