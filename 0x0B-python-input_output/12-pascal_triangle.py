#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """print pascatl triagle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        las = triangle[-1]
        nex = [1]

        for j in range(1, i):
            nex.append(las[j] + las[j - 1])
        nex.append(1)
        triangle.append(nex)

    return triangle
