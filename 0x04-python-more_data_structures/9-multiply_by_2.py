#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary[key] * 2
