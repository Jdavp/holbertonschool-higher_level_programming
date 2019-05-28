#!/usr/bin/python3
"""Module for a rectangle object"""


class Rectangle:
    """declaring class rectangle"""
    # A class variable, counting the number of instance
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialiazing rectagule with 2 parameters"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

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
        """setter for width"""
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
        return(self.__height * self.__width)

    def perimeter(self):
        """method to get perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """method to return a string of the object"""
        if self.__width == 0 or self.__height == 0:
            return("")
        imp = ""
        for i in range(self.__height):
            if i < self.height - 1:
                imp += self.__width * str(self.print_symbol) + '\n'
            else:
                imp += self.__width * str(self.print_symbol)
        return(imp)

    def __repr__(self):
        "method to return a string representation"
        return "Rectangle(" + str(self.height) + ',' + str(self.width) + ")"

    def __del__(self):
        """method to delete an instance and return a message)"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """method to compare 2 rectangules"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return(rect_2)
        else:
            return(rect_1)
