#! /usr/bin/env python3
# -*- coding: utf-8 -*-
mass =float(input("Please input your weight (kg)"))
height = float(input("Please input your height (m)"))
i =float(mass/(height**2))
print("Ваш BMI:" ,str(round(i)))
