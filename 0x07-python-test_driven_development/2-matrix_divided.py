#!/usr/bin/python3

"""
this module contains def matrix_divided
"""


def matrix_divided(matrix, div):
    """
    this function divides all elements of a matrix
    args:
        matrix: list of lists of ints or floats
        div: int or float
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row != matrix[0]:
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in row:
            if type(item) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
