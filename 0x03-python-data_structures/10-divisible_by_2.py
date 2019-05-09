#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new_list = []
    for i in range(len(my_list)):
        evaluation = my_list[i] % 2 == 0
        my_new_list.append(evaluation)
    return(my_new_list)
