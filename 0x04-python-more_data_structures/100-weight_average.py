#!/usr/bin/python3
def weight_average(my_list=[]):
    val1 = 0
    val = 0
    if my_list == None:
        break:
    for value, weight in my_list:
        val += value * weight
        val1 += weight
    return val / val1
