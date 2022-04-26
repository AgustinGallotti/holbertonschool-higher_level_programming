#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
    if (c >= 97 and c < 123):
        i = ord(i) - 32
        i = chr(i)
    print(f"{i}", end='')
