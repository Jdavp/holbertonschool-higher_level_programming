#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

'''script that adds all arguments to Python list and save them to a file'''
lista = []
try:
    x = load_from_json_file("add_item.json")
    for y in x:
        lista.append(y)
except:
    pass
for i in range(len(argv)):
    if i > 0:
        lista.append(argv[i])
save_to_json_file(lista, "add_item.json")
