#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = (a_dictionary.copy())
    if a_dictionary[key]:
        new_dict[key] = value
    else:
        return new_dict
