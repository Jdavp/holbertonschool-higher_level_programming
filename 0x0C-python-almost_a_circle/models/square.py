#!/usr/bin/python3
'''Class Square inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''declaring class square that inherits rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initializing square calling the super class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """method to return a string of the object"""
        return('[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y,
                                                 self.width))
