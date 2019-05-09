#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if largo == 0:
        return(largo, None)
    else:
        return(largo, sentence[0])
