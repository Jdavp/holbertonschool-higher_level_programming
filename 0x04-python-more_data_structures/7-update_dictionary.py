#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update = {key: value}
    for key, valuen in a_dictionary.items():
        a_dictionary.update(update)
        return(a_dictionary)
