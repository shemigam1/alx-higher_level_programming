#!/usr/bin/python3

"""matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        #check if row is a list
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        #check if the rows are the same length
        if row != matrix[0]:
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
        #check if the items of the rows are floats or int
        for item in row:
            if type(item) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if div is int or float
    if type(div) not in (float, int):
        raise TypeError("div must be a number")

    #check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by Zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
