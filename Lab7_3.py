#! /usr/bin/env python3
brackets = [ '[', ']','(', ')', '{', '}', '<', '>']

brackets_pairs = [brackets[_] + brackets[_ + 1] for _ in range(0, len(brackets), 2)]


def check_correct_count(calculation: str) -> bool:
    return calculation.count('(') == calculation.count(')') \
           and calculation.count('[') == calculation.count(']') \
           and calculation.count('{') == calculation.count('}') \
           and calculation.count('<') == calculation.count('>')


def drop(calculation: str) -> str:
    for i in brackets_pairs:
        calculation = calculation.replace(i, '')
    return calculation


def check(calculation: str) -> bool:
    calculation = ''.join(filter(lambda s: s in brackets, calculation))
    print(calculation)
    if check_correct_count(calculation):
        brackets_count = sum([calculation.count('('),
                              calculation.count('{'),
                              calculation.count('['),
                              calculation.count('<')])
        for _ in range(brackets_count):
            calculation = drop(calculation)
            if calculation == '':
                return True
    return False

print(check('auf(zlo)men [gy<psy>] four{s}'))