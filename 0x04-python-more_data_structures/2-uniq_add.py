#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    a = list(set(my_list))
    for i in a:
        suma += i
    return suma
