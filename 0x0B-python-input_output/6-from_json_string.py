#!/usr/bin/python3
import json
'''function that returns the JSON representation of an object (string)'''


def from_json_string(my_str):
    '''declarin object'''
    return json.loads(my_str)
