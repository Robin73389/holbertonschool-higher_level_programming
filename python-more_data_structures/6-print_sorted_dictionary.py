#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    key = {}
    key = a_dictionary

    key = sorted(key)

    for i, v in enumerate(key):
        print("{}: {}".format(key[i], a_dictionary[v]))
