#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Generate the next row by adding adjacent elements from the previous row
        prev_row = triangle[-1]
        new_row = [1]  # The first element is always 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)

    return triangle
