#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if sentence != None:
        return(largo, sentence[0])
    else:
        return(None)
