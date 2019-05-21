#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if True:
        try:
            print('{:d}'.format(value))
            return (True)
        except BaseException as a:
            print("Exception: {}".format(a), file=sys.stderr)
            return (False)
            pass
