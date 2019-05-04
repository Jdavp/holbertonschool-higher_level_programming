#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print('{} arguments:'.format(len(argv)-1))
    for it in range(len(argv)):
        if it > 0:
            print('{}: {}'.format(it, arguments[it]))
