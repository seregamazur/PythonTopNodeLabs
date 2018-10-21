#! /usr/bin/env python3

def find_longest(line: str) -> str:
    return ' '.join(sorted(line.split(), key=lambda word: len(word)))

line = input("Please input the line")
print(find_longest(line))