#!/usr/bin/env python3
# -*- coding: utf-8 -*-

seed = '054821'


def get_seed_numb(seed: str) -> list:
    return to_numb(seed)


def to_numb(s: str) -> list:
    return [int(n) for n in s]



def change_place_parts(numb: list) -> list:
    tmp = numb.copy()
    for _ in range(3):
        tmp.append(tmp.pop(0))
    return tmp


def remove_start_zeroes(numb: list) -> list:
    temp = numb.copy()
    while temp[0] == 0:
        temp.pop(0)
    return temp


def fill_start_zeroes(numb: list, to_position: int) -> list:
    temp = numb.copy()
    while temp.__len__() < to_position:
        temp.insert(0, 0)
    return temp

def get_random_int(seed: str):
    seed_numb = get_seed_numb(seed)
    after_change = change_place_parts(seed_numb)
    after_multiply = get_number_after_multiply(seed_numb, after_change)
    filled = fill_start_zeroes(after_multiply, 12)
    return slice_number(filled)


def get_number_after_multiply(a: list, b: list) -> list:
    a = int(''.join(map(str, remove_start_zeroes(a))))
    b = int(''.join(map(str, remove_start_zeroes(b))))
    return to_numb(str(a * b))


def slice_number(numb: list) -> int:
    temp = remove_start_zeroes(numb[3:9])
    return int(''.join(map(str, temp)))




def generate_random_int():
    global seed
    random_int = get_random_int(seed)
    seed = str(random_int)
    yield random_int


for _ in range(16):
    print(generate_random_int().__next__())