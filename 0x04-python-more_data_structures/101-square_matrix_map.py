#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix:
        return list(map(lambda i: list(map(lambda x: x ** 2, i)), matrix))
