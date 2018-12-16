#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import cos, sin


class FileReader:
    def __init__(self, path) -> None:
        self.path = path

    def lines(self) -> list:
        with open(self.path) as f:
            return [l.strip() for l in f.readlines()]


class Coordinates:
    def __init__(self, x: int, y: int) -> None:
        (self.x, self.y) = (x, y)


class Star:
    def __init__(self, name: str, coordinates: Coordinates) -> None:
        (self.name, self.coordinates) = (name, coordinates)

    @staticmethod
    def create(line: str):
        parts: list = line.split(' ')
        return Star(parts[0], Coordinates(int(parts[1]), int(parts[2])))

    def __str__(self) -> str:
        return f"{self.name}({self.coordinates.x}, {self.coordinates.y})"

    def rotate(self, __angle: float) -> None:
        self.coordinates.x = round(self.coordinates.x * cos(__angle) - self.coordinates.y * sin(__angle))
        self.coordinates.y = round(self.coordinates.x * sin(__angle) + self.coordinates.y * cos(__angle))


def parse_angle(__lines: list):
    return float(str(__lines.pop(0)).split(' ')[1])


fileReader: FileReader = FileReader("file.txt")
lines: list = fileReader.lines()
angle: float = parse_angle(lines)
print(angle)
stars: list = list(map(Star.create, lines))
for star in stars:
    star.rotate(angle)

stars.sort(key=lambda s: (s.coordinates.y, s.coordinates.x))
print()
for star in stars:
    print(star)