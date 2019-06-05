#!/usr/bin/python3
'''Module for mylist object'''


class MyList(list):
    '''declaring my list'''
    def print_sorted(self):
        copy = self.copy()
        copy.sort()
        print(copy)
