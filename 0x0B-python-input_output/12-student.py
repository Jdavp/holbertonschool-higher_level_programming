#!/usr/bin/python3
'''Write a class Student that defines a student'''


class Student:
    '''declaring a class student'''
    def __init__(self, first_name, last_name, age):
        '''initial class variables'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method to return a dictionary of the object'''

        dic = {}
        if type(attrs) is list:
            for keys, value in self.__dict__.items():
                for x in attrs:
                    if keys == x:
                        dic[keys] = value
            return dic
        else:
            return self.__dict__
