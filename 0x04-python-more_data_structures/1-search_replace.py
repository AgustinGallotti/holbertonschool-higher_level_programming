#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = (my_list.copy())
    for search, item in enumerate(new):
        if item == search:
            new[search] = replace
    return new
