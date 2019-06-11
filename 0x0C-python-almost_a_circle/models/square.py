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

    def update(self, *args, **kwargs):
        '''update attributes'''
        if args is None or len(args) == 0:
            for key, value in kwargs.items():

                if key == 'id':
                    self.id = value

                if key == "size":
                    self.height = value
                    self.width = value

                if key == 'x':
                    self.x = value

                if key == 'y':
                    self.y = value

        else:

            for ite in range(len(args)):

                if ite == 0:
                    self.id = args[ite]

                if ite == 1:
                    self.height = args[ite]
                    self.widht = args[ite]

                if ite == 2:
                    self.x = args[ite]

                if ite == 3:
                    self.y = args[ite]

    def to_dictionary(self):
        '''method to return the directory representation of the object'''
        return{'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
