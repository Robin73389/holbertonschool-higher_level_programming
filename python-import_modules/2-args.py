#!/usr/bin/python3

import sys


if __name__ == "__main__":

    nb = (len(sys.argv) - 1)

if nb == 0:
    print("0 arguments.")
elif nb == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(nb))

for i, nb in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, nb))
