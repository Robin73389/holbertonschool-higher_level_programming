#!/usr/bin/python3

import sys

nb = (len(sys.argv) - 1)
mot = "argument:" if nb == 1 else "arguments."

print("{} {}".format(nb, mot))

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
