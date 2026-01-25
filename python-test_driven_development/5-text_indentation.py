#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    ligne = ""

    for c in text:
        ligne = ""
        ligne += c

        if c in ('.', '?', ':'):
            print(ligne)
            print()
        else:
            print(c, end='')
