#! /usr/bin/env python3
# -*- coding: utf-8 -*-
def pairs(a, b, c):
    return [(a, b), (b, a),
            (c, b), (b, c),
            (a, c), (c, a)]


def fit():
    for l1, l2 in a:
        if l1 <= h and l2 <= w:
            return True
    return False


h,w = input("Input sizes of the door:").split()
a,b,c = input("Input sizes of the box:").split()
a = pairs(a,b,c)
print(fit())
