#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nuevalista = []
    div = 0
    y = 0
    for y in range(list_length):
        try:
            div = my_list_1[y] / my_list_2[y]
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            nuevalista.append(div)
    return nuevalista
