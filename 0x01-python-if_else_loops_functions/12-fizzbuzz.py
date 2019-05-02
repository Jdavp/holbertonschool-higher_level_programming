#!/usr/bin/python3
def fizzbuzz():
    for s in range(1, 101):
        print('Fizz' * (s % 3 == 0) + 'Buzz' * (s % 5 == 0) or s, end=" ")
