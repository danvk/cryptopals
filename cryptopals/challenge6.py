#!/usr/bin/env python

def edit_distance(bits1, bits2):
    assert len(bits1) == len(bits2)
    return sum(
        1 if b1 != b2 else 0
        for b1, b2 in zip(bits1, bits2)
    )


