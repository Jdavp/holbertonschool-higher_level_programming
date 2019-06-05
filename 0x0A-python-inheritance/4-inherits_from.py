#!/usr/bin/python3
'''function returns if the object is an instance of a class that inherited'''


def inherits_from(obj, a_class):
    '''definite and instance in an object'''
    if type(obj) == a_class:
        return False
    else:
        return (issubclass(type(obj), a_class))
