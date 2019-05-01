#!/usr/bin/python3
final = ", "
for n in range(00, 100):
    if n < 10:
        print("{}{}".format(0, n), end=final)
    if n > 9:
        if n == 99:
            final = "\n"
        print(n, end=final)
