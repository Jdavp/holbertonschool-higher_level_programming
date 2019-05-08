#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    listaa = (tuple_a) + (0,0)
    listab = (tuple_b) + (0,0)
    resultado = (listaa[0] + listab[0], listaa[1] + listab[1])
    print(resultado)
