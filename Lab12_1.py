#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt


class Point:
    x: float
    y: float


    def distance(self, point) -> float:
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def __init__(self, x: float, y: float) -> None:
        (self.x, self.y) = (x, y)



class Side:
    def __init__(self, p1: Point, p2: Point) -> None:
        (self.p1, self.p2) = (p1, p2)

    def length(self) -> float:
        return self.p1.distance(self.p2)


class Triangle:
    p1: Point
    p2: Point
    p3: Point

    s1: Side
    s2: Side
    s3: Side

    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        (self.p1, self.p2, self.p3) = (p1, p2, p3)
        (self.s1, self.s2, self.s3) = (Side(p1, p2), Side(p2, p3), Side(p1, p3))

    def is_exist(self) -> bool:
        a = self.s1.length()
        b = self.s2.length()
        c = self.s3.length()
        return (a + b > c) and (b + c > a) and (a + c > b)


point1 = Point(1, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)
triangle = Triangle(point1, point2, point3)

print(triangle.is_exist())
