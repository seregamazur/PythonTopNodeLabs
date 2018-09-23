#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import sqrt,exp, pi

def formule(x, h, q):
    if x==0 or h==0 or q==0:
      return 0 
    else:
      return 1 / (q * sqrt(2 * pi)) * exp(-((x - h) ** 2) / 2 * q ** 2)


def get_arr():
    print("Input 3  numbs")
    return  float(input("x=")), float(input("h=")),float(input("q="))


arr = get_arr()
res = formule(arr[0], arr[1],arr[2])
print('{:0.10f}'.format(res))
