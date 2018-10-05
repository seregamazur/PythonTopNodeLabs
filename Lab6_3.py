#!/usr/bin/env python3
# *-*coding: utf-8 *-*


def formule(sum: int, insum: int, years: int) -> float:
    """This function return formule in  float"""
    return sum * (1 + percent / 100) ** years

def calculate(sum: int, insum: int, perc: int) -> int:
    """This function return result years"""
    result = 0
    while formule(sum, insum, result) < insum:
        result += 1
    return result

def input_ui():
    """This function return inputted nums"""
    sum,insum,percent = input("Please enter sum you have,interest sum and percent:").split()
    return float(sum), float(insum), float(percent)

sum,insum,percent = input_ui()
print("You have to wait ",calculate(sum,insum,percent)," years.")