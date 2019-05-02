#!/usr/bin/python3
def uppercase(str):
    strfinal = ""
    for l in str:
        if ord(l) >= 97 and ord(l) <= 122:
            strfinal += (chr(ord(l) - 32))
        else:
            strfinal += l
    print(strfinal)
