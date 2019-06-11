#!/usr/bin/python3
'''the first class Base'''
import json


class Base:
    '''declaring a base clase'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initializing the base case with id attributes'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method returns the JSON string representation'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''method writes the JSON string representation of a file'''
        nueval = []

        for y in list_objs:
                nueval.append(cls.to_dictionary(y))
        with open(cls.__name__+'.json', mode="w") as f:
            f.write(Base.to_json_string(nueval))
