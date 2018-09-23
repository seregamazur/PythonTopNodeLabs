#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import sqrt,e

def formule(a, b):
    if b==0:
      return 0 
    else:
      return ((sqrt(a * b)) / (e ** a * b)) + (a * e ** (2 * a / b))


def get_arr():
    print("Input 2  numb a&b where b !=0")
    return  float(input("a=")), float(input("b="))


arr = get_arr()
res = formule(arr[0], arr[1])
print('{:0.12f}'.format(res))
