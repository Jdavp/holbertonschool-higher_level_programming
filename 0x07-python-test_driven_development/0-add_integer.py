#!/usr/bin/python3
"""Module to add to integers
"""


def add_integer(a, b=98):
    """Function to add 2 integers or floats and return a integer
    """
    if type(a) is not int and type(a) is not float or a is None:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
