#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda n: list((map(lambda a: a * a, n)))), matrix))
