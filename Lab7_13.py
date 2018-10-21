#! /usr/bin/env python3
def check(line1: str,line2: str) -> bool:
    for i in list(line2):
        if line1.count(i) < line2.count(i):
            return "No"
    else:
        return "Yes"
line1 = input("Please input the first string symbols:")
line2 = input("Please input the second string symbols:")
print("Can we create same sentence as first from the second string?",check(line1,line2))