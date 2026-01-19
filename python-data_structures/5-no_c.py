#!/usr/bin/python3

def no_c(my_string):
    res = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            res += s
    return res
