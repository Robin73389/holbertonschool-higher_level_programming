#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for line in matrix:
        new_line = []

        for valeur in line:
            carré = valeur * valeur
            new_line.append(carré)

        new_matrix.append(new_line)

    return new_matrix
