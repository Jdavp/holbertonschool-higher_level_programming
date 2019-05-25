#!/usr/bin/python3
"""Module to print #
"""


def print_square(size):
    """Function to print # to given numbers of size
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        print((i == size) * '#', end="")
        print(size * '#')
