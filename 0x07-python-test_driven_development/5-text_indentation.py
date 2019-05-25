#!/usr/bin/python3
def text_indentation(text):
    i = 0
    if type(text) is not str:
        raise TypeError('text must be a string')
    while i < len(text):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            i = i + 1
            print("\n")
        i+=1
