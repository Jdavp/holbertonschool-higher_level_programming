#!/usr/bin/python3
'''the class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''declaring clase rectangle that inherir from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializing reactagle with attributes'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for heigth"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('heigth must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' method to find the area'''
        return(self.__height * self.__width)

    def display(self):
        '''method to display a character'''
        print(self.__height * "\n", end="")
        for y in range(self.width):
            print(self.height * " ", end="")
            print(self.width * '#')

    def __str__(self):
        """method to return a string of the object"""
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x, self.y,
                                                       self.__width,
                                                       self.__height))
