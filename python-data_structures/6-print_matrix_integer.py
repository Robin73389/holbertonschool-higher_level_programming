#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for a in matrix:
        D_matrix = ""
        for i in a:
            D_matrix += str(i) + " "
        print("{:d}".format(D_matrix))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
