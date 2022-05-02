#!/usr/bin/python3
a = 89
b = 10
if a:
    if b:
        a, b = b, a
        print("a={:d} - b={:d}".format(a, b))
else:
    print("error in match")
