#! /usr/bin/env python3
def divide(number: str) -> tuple:
    length = len(number)
    half = length // 2
    left = number[:half]
    if length % 2 == 0:
        right = number[half:]
    else:
        right = number[half + 1:]
    return left, right


def is_lucky(number: str) -> str:
    (left, right) = divide(number)
    left_sum = sum(map(lambda a: int(a), left))
    right_sum = sum(map(lambda a: int(a), right))
    if left_sum == right_sum:
        return "Lucky"
    else:
        return "Unlucky..."

num = input("Please input an number of your ticket:")
print(is_lucky(num))