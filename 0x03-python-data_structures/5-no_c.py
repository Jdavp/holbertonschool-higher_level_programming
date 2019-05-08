#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        return (my_string.translate({ord(i): None for i in 'c, C'}))
