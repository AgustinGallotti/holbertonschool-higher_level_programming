#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(my_list)
    for search, item in enumerate(my_list):
        if item == search:
            new[search] = replace
    return new
