#!/usr/bin/python3
"""module for function to divide a matrix"""


def matrix_divided(matrix, div):
    """divided"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) is not list:
        raise TypeError(error)

    newmatrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        newrow = []
        for b in row:
            if type(b) is not int and type(b) is not float:
                raise TypeError(error)
            newrow.append(round(float(b / div), 2))
        newmatrix.append(newrow)
    return newmatrix
