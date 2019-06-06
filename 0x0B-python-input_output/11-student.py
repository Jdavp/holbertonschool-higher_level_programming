#!/usr/bin/python3
'''Write a class Student that defines a student'''


class Student:
    '''declaring a class student'''
    def __init__(self, first_name, last_name, age):
        '''initial class variables'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method to return a dictionary of the object'''
        return self.__dict__
