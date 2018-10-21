#! /usr/bin/env python3
def find_shortest(line: str) -> str:

    return min(line.split(),key = len)

line = input("Please input the sentence:")
print(find_shortest(line))