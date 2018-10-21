#! /usr/bin/env python3
vowels1 = "a e i o y u "
def vowels(line: str) -> int:
    numb = 0
    line = line.lower()
    for _ in list(line):
        if _ in list(vowels1):
            numb +=1
    return numb

line = input("please input the line:")
print("There is ",vowels(line), " vowels.")