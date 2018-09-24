#! /usr/bin/env python3
# -*-coding: utf-8 -*-
a,b,c = input("Input 3 sides of triangle:").split()
def conditions(a,b,c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
      print("Exist")
    else:
      print("does Not exist")
conditions(a,b,c)
