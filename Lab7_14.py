#! /usr/bin/env python3
import re
mail = input("Please enter your email:")
result = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
if not result.match(mail):
    print("false")
else: 
    print("True")
