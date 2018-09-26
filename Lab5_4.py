#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
from cmath import sqrt as complex_sqrt

def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    print(f'Discriminant = {discriminant}')
    if discriminant < 0:
        x1 = (-b / (2 * a)) - ((1j* complex_sqrt(-discriminant)) / (2 * a))
        x2 = (-b / (2 * a)) + ((1j* complex_sqrt(-discriminant)) / (2 * a))
        print(f"[x1={x1}, x2={x2}]")
    else:
        if a == 0:
            print("There is no root")
        elif discriminant > 0:
            x1 = (-b - sqrt(discriminant)) / 2 * a
            x2 = (-b + sqrt(discriminant)) / 2 * a
            '{:0.4f}'.format(x1)
            '{:0.4f}'.format(x2)
            print(f'[x1 = {x1}, x2 = {x2}]')
        else:
            x = -b / (2 * a)
            print(f'x = {x}')
a,b,c = [float(s) for s in input("Please input a,b,c:").split()]
print(f"a={a};b={b};c={c}")
roots(a, b, c)
