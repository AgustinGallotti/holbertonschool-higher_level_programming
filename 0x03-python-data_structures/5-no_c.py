#!/usr/bin/python3
def no_c(my_string):
    a = {'c': None, 'C': None}
    b = my_string.maketrans(a)
    z = my_string.translate(b)
    return (z)
