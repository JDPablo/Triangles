"""part of a homework assignment: see function docstring below"""
import math


def classify_triangle(side_a, side_b, side_c):
    """inputs 3 values for triangle sides and classifies the type of triangle"""
    triangle_type = ""
    if side_a == side_b == side_c:
        triangle_type = "equilateral"
    elif (side_a == side_b != side_c) or (side_a != side_b == side_c):
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    if side_a*side_a + side_b*side_b == side_c*side_c:
        triangle_type += " and right"
    return triangle_type

print(classify_triangle(3, 4, 5))
print(classify_triangle(2, 2, 2))
print(classify_triangle(3, 3, math.sqrt(18)))
