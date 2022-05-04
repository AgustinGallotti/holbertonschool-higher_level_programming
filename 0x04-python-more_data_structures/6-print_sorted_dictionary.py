#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = a_dictionary
    for key, value in sorted(d.items()):
        print (f"{key}: {value}")
