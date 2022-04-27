#!/usr/bin/env python3
def print_last_digit(number):

    if (number > 0):
        r = number % 10
    else:
        r = (number * -1) % 10
    print(f"{r}", end='')
    return(r)
