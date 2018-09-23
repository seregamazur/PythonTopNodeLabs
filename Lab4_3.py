#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal

salary = input("Your salary : ")
tax = Decimal(salary) *  Decimal('0.18')
wartax = Decimal(salary)*Decimal('0.015')
alltax = tax +  wartax
print("You need to pay:",alltax,"tax")
print("Your clean salary is:",Decimal(salary)-alltax)
