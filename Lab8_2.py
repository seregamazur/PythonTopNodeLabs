#!/usr/bin/env python3
def quick_sort(arr: list) -> list:
    if len(arr) < 1:
        return arr
    start = arr[0]
    left = []
    right = []
    for x in range(1, len(arr)):
        if arr[x] <= start:
            left.append(arr[x])
        else:
            right.append(arr[x])
    left = quick_sort(left)
    right = quick_sort(right)
    a = [start]
    return left, a, right


arr = [int(x) for x in input("Please input an array:").split()]
print(quick_sort(arr))
