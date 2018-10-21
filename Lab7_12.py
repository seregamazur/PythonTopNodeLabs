#! /usr/bin/env python3

def del_spaces(line: str) -> str:
    return " ".join(line.split())
line = input("Please input the line")
print(del_spaces(line))