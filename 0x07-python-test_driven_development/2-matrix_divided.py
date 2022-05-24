#!/usr/bin/python3
"""module for function to divide a matrix"""


def matrix_divided(matrix, div):
    """divided"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integer/floats")

    rowlenght = len(matrix[0])
    newmatrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != rowlenght:
            raise TypeError("Each row of the matrix must have the same size")
        newrow = []
        for i in matrix:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integer/floats")
            if len(i) != len(matrix[0]):
                raise TypeError("Each row of the matrix must be have \
                                the same size")
            newrow.append(round(float(x / div), 2))
        newmatrix.append(newrow)
    return newmatrix
