#!/usr/bin/python3
'''the first class Base'''


class Base:
    '''declaring a base clase'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initialazing the base case with id attributes'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
