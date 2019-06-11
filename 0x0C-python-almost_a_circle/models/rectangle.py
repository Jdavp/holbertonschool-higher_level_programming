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
            raise ValueError('height must be > 0')
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
        print(self.__y * "\n", end="")
        for i in range(self.__height):
                print(self.__x * " ", end="")
                print(self.__width * '#')

    def __str__(self):
        """method to return a string of the object"""
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height))

    def update(self, *args, **kwargs):
        '''method to update attributes'''

        if args is None or len(args) == 0:
            for key, value in kwargs.items():

                if key == 'id':
                    super().__init__(value)

                if key == "width":
                    self.__width = value

                if key == "height":
                    self.__height = value

                if key == 'x':
                    self.__x = value

                if key == 'y':
                    self.__y = value

        else:

            for ite in range(len(args)):

                if ite == 0:
                    self.id = args[ite]

                if ite == 1:
                    self.__width = args[ite]

                if ite == 2:
                    self.__height = args[ite]

                if ite == 3:
                    self.__x = args[ite]

                if ite == 4:
                    self.__y = args[ite]

    def to_dictionary(self):
        '''method to return the directory representation of the object'''
        return{'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
               'width': self.width}
