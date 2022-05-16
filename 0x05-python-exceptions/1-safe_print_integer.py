#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if type(value) == int:
            printf("{:d}".format, value)
            return True
    except:
        if type(value != int):
            return False
