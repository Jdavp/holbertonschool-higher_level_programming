#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if sentence is not None:
        return(largo, sentence[0])
    elif len(sentence) == 0:
        return None
