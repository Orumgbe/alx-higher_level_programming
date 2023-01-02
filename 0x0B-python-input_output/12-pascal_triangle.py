#!/usr/bin/python3
"""12-pascal_triangle, pascal_triangle()"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing pascal's triangle"""
    p_triangle = []
    if (n <= 0):
        return p_triangle
    else:
        for i in range(n):
