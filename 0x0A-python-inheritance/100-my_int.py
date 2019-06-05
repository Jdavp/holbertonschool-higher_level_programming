#!/usr/bin/python3
'''Write a class MyInt that inherits from int'''


class MyInt(int):
    def __init__(self, value):
        '''initialize value'''
        self.value = value

    def __eq__(self, other):
        '''initalize module eq to mirror results'''
        print(self.value == other)
