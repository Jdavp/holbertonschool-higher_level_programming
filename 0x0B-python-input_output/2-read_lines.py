#!/usr/bin/python3
'''function that reads n lines of a text file (UTF8) and prints it to stdout'''


def read_lines(filename="", nb_lines=0):
    '''reading a file'''
    with open(filename, encoding= "utf-8") as myFile:

        for i in range(nb_lines):
           print(myFile.readline(), end="")
        if nb_lines <= 0 or nb_lines >= len(myFile.readlines()):
            print(myFile.read(), end="")
