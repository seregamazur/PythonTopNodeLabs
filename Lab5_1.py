#! /usr/bin/env python3
# -*-coding: utf-8 -*-
a=int(input("a="))
def is_power2(a):
    return ((a & (a - 1)) == 0) and a > 0   
print(is_power2(a))

