#!/usr/bin/env python3

def answer(people,k: int) -> int:
    tmp = 0
    while len(people) > 1:
        tmp += 1
        item = people.pop(0)
        if tmp != 3:
            people.append(item)
        else:
            print(item," soldier die")
            tmp = 0
    return people

soldiers = list(range(1, int(input("Please input the number of soldiers:")) + 1))
k = int(input("Please input count :"))
print(answer(soldiers,k))