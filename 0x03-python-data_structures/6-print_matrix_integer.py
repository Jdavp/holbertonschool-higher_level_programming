#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        if matrix != [[]]:
            columns = len(matrix)
            for y in range(columns):
                for x in range(len(matrix[y]) - 1):
                    print("{:d}".format(matrix[y][x]), end=' ')
                x += 1
                print("{:d}".format(matrix[y][x]))
        else:
            print()
