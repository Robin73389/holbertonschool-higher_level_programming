#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for a in matrix:
        D_matrix = ""
        for i in a:
            D_matrix += str(i) + " "
        print("{:s}".format(D_matrix))
