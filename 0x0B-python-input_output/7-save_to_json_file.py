#!/usr/bin/python3
import json
'''function that writes an Object to a text file using a JSON representation'''


def save_to_json_file(my_obj, filename):
    '''declarin object'''
    with open(filename, mode="a", encoding="utf-8") as f:
        json.dump(my_obj, f)
