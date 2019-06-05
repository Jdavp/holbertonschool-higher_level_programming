#!/usr/bin/python3
'''Write an empty class BaseGeometry'''


class BaseGeometry:
    '''declarin a class BaseGeometry'''
    def area(self):
        ''' method to find the area'''
    raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''method to validate values'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    '''declaring a class Rectangle'''
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__heigh = height
