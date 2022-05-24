#!/usr/bin/python3
"""module for function to divide a matrix"""

def matrix_divided(matrix, div):
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                       " of integers/floats")
    if type(div) is not float or type(div) is not int:
        raise TypeError("div must be an number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integer/floats")
    newrow = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integer/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must be have \
                            the same size")
        newrow.append(round(float(x / div), 2))
    newmatrix.append(newrow)
    return newmatrix
