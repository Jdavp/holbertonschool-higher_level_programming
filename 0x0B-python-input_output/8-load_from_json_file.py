#!/usr/bin/python3
import json
'''function that writes an Object to a text file using a JSON representation'''


def load_from_json_file(filename):
    '''declarin object'''
    with open(filename)as f:
        return(json.load(f))
