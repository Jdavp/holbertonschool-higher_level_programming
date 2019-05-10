#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nueva = []
    for x in matrix:
        segunda = []
        for item in x:
            segunda.append(item * item)
        nueva.append(segunda)
    return nueva
