#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import factorial


def IsPrime(n):
    if (factorial(n - 1) + 1) % n != 0:  
        print("No")
    else:
        print("Yes")


n = int(input())
IsPrime(n)
