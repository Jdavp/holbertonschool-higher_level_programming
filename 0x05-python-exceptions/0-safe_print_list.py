#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    contador = 0
    for i in my_list:
        try:
            if contador < x:
                print(i, end='')
                contador += 1

        except IndexError:
            pass
    print()
    return(contador)
