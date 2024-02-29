#!/usr/bin/env python

from cryptopals.challenge5 import str_to_bits
from cryptopals.challenge6 import edit_distance


def test_edit_distance():
    bits1 = str_to_bits('this is a test')
    bits2 = str_to_bits('wokka wokka!!!')
    assert edit_distance(bits1, bits2) == 37
