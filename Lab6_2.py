#!/usr/bin/env python3
# *-*coding: utf-8 *-*


def formule(sum: int, perc: int, years: int) -> float:
    """This function return formule in  float"""
    return float((sum*(1+perc/100*years)))

def calculate(sum: int, perc: int, years: int) -> int:
    """This function return result """
    result = formule(sum,perc,years)
    return '₴{:,.2f}'.format(result)

def input_ui():
    """This function return inputted nums"""
    sum,perc,years = input("Please enter your sum,interest rate and years:").split()
    return float(sum), float(perc), float(years)

sum,perc,years = input_ui()
print(calculate(sum,perc,years))