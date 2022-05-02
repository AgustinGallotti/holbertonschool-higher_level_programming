#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp2 = list(my_list)
    if idx < 0:
        return cp2
    elif idx >= len(my_list):
        return cp2
    else:
        cp_list = list(my_list)
        cp_list[idx] = element
        return cp_list
