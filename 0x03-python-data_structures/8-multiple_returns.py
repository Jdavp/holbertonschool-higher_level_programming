#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if sentence is not None:
        return(largo, sentence[0])
    elif largo == 0:
        return(largo, None)
