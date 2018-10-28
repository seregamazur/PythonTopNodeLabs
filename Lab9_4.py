#! /usr/bin/env/python 3


roman_numbers = {
    1: 'I',2: 'II',3: 'III',4: 'IV', 5: 'V',
    6: 'VI',7: 'VII', 8: 'VIII',9: 'IX',10: 'X',
    20: 'XX',30: 'XXX',40: 'XL',50: 'L',60: 'LX',
    70: 'LXX', 80: 'LXXX',90: 'XC',100: 'C',200: 'CC',
    300: 'CCC',400: 'CD',500: 'D',600: 'DC',700: 'DCC',
    800: 'DCCC',900: 'CM',1000: 'M',2000: 'MM',3000: 'MMM'
}

def to_pow(position: int, digits: list) -> int:
    digit_pow = (len(digits) - 1 - position)
    return digits[position] * (10 ** digit_pow)

def convert(arabic_number: int) -> str:
        digits = list(map(int, str(arabic_number)))
        digits_in_power = list(map(lambda i: to_pow(i, digits), range(0, len(digits))))
        rome_digits = list(map(lambda i: roman_numbers[i], digits_in_power))
        return ''.join(rome_digits).upper()

print(convert(15))