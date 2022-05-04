#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
    n = [roman[i] for i in roman_string.lower() if i in roman]
    return sum([i if i>=n[min(j+1, len(n)-1)] else -i for j,i in enumerate(n)])
