#!/usr/bin/python3
"""Module for a rectangule object"""


class Rectangle:
    """declaring class rectangule"""
    def __init__(self, width=0, height=0):
        """initialiazing rectagule with 2 parameters"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for heigth"""
        return self.__height

    @width.setter
    def width(self, value):
        """getter for heigth"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError('heigth must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method to get area"""
        return(self.height * self.width)

    def perimeter(self):
        """method to get perimeter"""
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((self.height * 2) + (self.width * 2))
