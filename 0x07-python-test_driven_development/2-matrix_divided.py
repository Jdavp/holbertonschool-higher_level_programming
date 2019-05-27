#!/usr/bin/python3
""" Module to divide all the items of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divide all the in a matrix for a given number
    """
    te1 = 'matrix must be a matrix (list of lists) of integers/floats'
    te2 = 'Each row of the matrix must have the same size'
    nueva = []
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for x in matrix:
        segunda = []
        for item in x:
            if type(item) is not int and type(item) is not float:
                raise TypeError(te1)
            if len(matrix[0]) != len(x):
                raise TypeError(te2)
            segunda.append(round(item / div, 2))
        nueva.append(segunda)
    return nueva
