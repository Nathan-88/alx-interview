#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in every row is always 1
        if triangle:  # If not the first row
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element in every row is always 1
        triangle.append(row)

    return triangle
