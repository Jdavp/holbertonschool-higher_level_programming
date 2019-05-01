#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of "
greater = " and is greater than 5 "
zero = " and is 0 "
less = " and is less than 6 an not 0 "
lastdigit = 0
if number > 0:
    lastdigit = number % 10
if number < 0:
    lastdigit = number % -10
if lastdigit > 5:
    print("{}{} is {}{}".format(string, number, lastdigit, greater), end='\n')
elif lastdigit == 0:
    print("{}{} is {}{}".format(string, number, lastdigit, zero), end='\n')
elif lastdigit < 6:
    print("{}{} is {}{}".format(string, number, lastdigit, less), end='\n')
