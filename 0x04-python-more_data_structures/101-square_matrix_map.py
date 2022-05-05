#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row = map(lambda n: n * n, matrix[i])
        new_matrix.append(list(row))
    return new_matrix   
