#!/usr/bin/python3
'''function that returns the number of lines of a text file:'''


def number_of_lines(filename=""):
    '''reading a file'''
    with open(filename, encoding= "utf-8") as myFile:

        i = 0
        for c in myFile.readlines():
            i += 1
        return(i)
