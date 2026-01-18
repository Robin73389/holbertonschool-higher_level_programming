#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        x = ord(c)
        if 97 <= x <= 122:
            result += chr(x - 32)
        else:
            result += c
    print("{}".format(result))
