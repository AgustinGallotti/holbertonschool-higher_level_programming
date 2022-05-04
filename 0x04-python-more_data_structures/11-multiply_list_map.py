#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = (my_list.copy())
    new_list = [x*number for x, nubmer in zip(my_list, new_list)]
    return new_list
