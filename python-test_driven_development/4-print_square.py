#!/usr/bin/python3

def print_square(size):
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        i = i
        print("#" * size)

    print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")