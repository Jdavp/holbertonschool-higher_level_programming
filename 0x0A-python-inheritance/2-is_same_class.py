#!/usr/bin/python3
'''function that returns if the object is an instance of the specified class'''


def is_same_class(obj, a_class):
    '''definicion of obj and class'''
    if type(obj) == a_class:
        return True
    else:
        return False
