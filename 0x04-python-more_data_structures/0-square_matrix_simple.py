#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[element**2 for element in row] for row in matrix]
    return new
