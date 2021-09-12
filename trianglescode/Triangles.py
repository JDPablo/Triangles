import unittest
import math


def classify_triangle(a, b, c):
    triangle_type = ""
    if a == b == c:
        triangle_type = "equilateral"
    elif (a == b != c) or (a != b == c):
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    if a*a + b*b == c*c:
        triangle_type += " and right"
    return triangle_type

print(classify_triangle(3, 4, 5))
print(classify_triangle(2, 2, 2))
print(classify_triangle(3, 3, math.sqrt(18)))