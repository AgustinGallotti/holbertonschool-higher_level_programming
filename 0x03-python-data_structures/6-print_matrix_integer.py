#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in item:
            print(j, end=" " if j != item[-1] else "")
        print("")
