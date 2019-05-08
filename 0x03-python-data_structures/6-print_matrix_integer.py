#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        if matrix != [[]]:
            columns = len(matrix)
            rows = len(matrix[0])
            for y in range(rows):
                for x in range(columns - 1):
                    print("{:d}".format(matrix[y][x]), end=' ')
                    x += 1
                print('{:d}'.format(matrix[y][x]))
        else:
            print()
