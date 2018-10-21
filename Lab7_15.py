#! /usr/bin/env python3
import random
import string
symbols = r"~ ! @ # $ % ^ & * ( ) _ + ` - = { } [ ] : ; < > . \ /".replace(' ', '')

def password() -> str:
    letters = [random.choice(string.ascii_letters) for _ in range(random.randint(8, 8))]
    digits = random.choice(string.digits)
    special_symbols = random.choice(symbols)
    digsym = digits + special_symbols
    generated = letters + digsym.split()
    return ''.join(generated)
print(password())