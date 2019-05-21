#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        fct(*args)
    except BaseException as a:
        fct = None
        print("Exception: {}".format(a), file=sys.stderr)
    return fct(*args)
