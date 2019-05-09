#!/usr/bin/python3
def max_integer(my_list=[]):
    largo = len(my_list)
    my_list.sort()
    if largo == 0:
        return(None)
    else:
        return(my_list[-1])
