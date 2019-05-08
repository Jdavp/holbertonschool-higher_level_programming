#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        if matrix != [[]]:
            columns = len(matrix)
            rows = len(matrix[0])
            pad_len = len(str(rows * columns)) + 1
            for y in range(rows):
                for x in range(columns):
                    print("{n:>{pad}}".format(n=y * columns + x + 1,
                                              pad=pad_len),
                          end='')
                print()
        else:
            print()
