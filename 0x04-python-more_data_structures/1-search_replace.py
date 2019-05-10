#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    nueva = my_list.copy()
    for i in range(len(nueva)):
        if search == nueva[i]:
            nueva[i] = replace
    return nueva
