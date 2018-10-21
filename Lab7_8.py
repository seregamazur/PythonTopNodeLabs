#! /usr/bin/env python3

def out(value: int) -> str:
    if value % 3 == 0 and value % 5 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    return str(value)

for i in range(1, 101):
    print(out(i))