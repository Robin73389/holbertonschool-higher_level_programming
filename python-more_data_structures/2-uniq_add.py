#!/usr/bin/python3

def uniq_add(my_list=[]):

    somme = 0
    unique = set(my_list)

    for valeur in unique:
        somme = somme + valeur
    return somme
