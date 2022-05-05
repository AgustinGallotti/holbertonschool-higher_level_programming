#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        val = 0
        val1 = 0
        for value, weight in my_list:
            val += value * weight
            val1 += weight
        return val / val1
    else:
        return 0
