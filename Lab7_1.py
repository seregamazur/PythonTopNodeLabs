#!/usr/bin/env python3
# *-*coding: utf-8 *-*
line: str = input("Input the line:")
shift: int = int(input("Input the numb of shift:"))

after = line[:shift]
before = line[shift:]
print(before + after)
