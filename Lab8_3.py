#!/usr/bin/env python3

def average_med(arr: list) -> list:
    suma = sum(arr)
    average = suma/len(arr)
    median = len(arr)//2
    result = sorted(arr)[median]
    return average,result

arr = [int(x) for x in input("Please input an array:").split()]
print(average_med(arr))