#!/usr/bin/env python3
# *-*coding: utf-8 *-*

from math import sqrt


def half_per(a: int, b: int, c: int) -> float:
    """This function return half perimetr float"""
    return float(((a + b + c) / 2))


def calculate(a: int, b: int, c: int) -> int:
    """This function return result of heron formule"""
    p = half_per(a, b, c)
    return sqrt(p * (p - a) * (p - b) * (p - c))


def input_ui():
    """This function return inputted abc"""
    a, b, c = input("Please enter 3 sides of triangle").split()
    return float(a), float(b), float(c)

if __name__== '__main' :
    a, b, c = input_ui()
    print(calculate(a, b, c))

