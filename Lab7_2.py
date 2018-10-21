#! /usr/bin/env python3
import re
def contains_digsym(data: str) -> str:
    return re.sub(r'[^A-Z]+', r'', data).lower()

def check():
    data = str(input("Please enter the string:"))
    result = contains_digsym(data)
    return result == ''.join(reversed(result))

print(check())
