#! /usr/bin/env python3
def increase_shifr(line: str) -> str:
    if ord('Z') == ord(line):
        return 'A'
    elif ord('z') == ord(line):
        return 'a'
    return chr(ord(line) + 1)


line = input("Please input the line")
word = list(line)
word = map(lambda s: increase_shifr(s), word)
print(''.join(word))