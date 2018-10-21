#! /usr/bin/env python3

def output(line: str) -> str:
    out= '*' *  (len(line)+4)
    return '{0}\n* {1} *\n{2}'.format(out, line, out)

print(output("Hello"))
