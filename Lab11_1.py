#! /usr/bin/env/python 3
# -*- coding: utf-8 -*-


def readl():
    file = "2017_05_07_nginx.txt"
    f = open(file,"r")
    for line in f:
        yield line


def get_bytes_line(line: str) -> int:
    return int(line.split()[9])

line = readl()
getByte = 0
postByte = 0
for i in line:
    data = get_bytes_line(i)
    if i.__contains__('GET'):
        getByte += data
    elif i.__contains__('POST'):
        postByte += data

print(f'GET: = {getByte}')
print(f'POST: = {postByte}')
readl()
