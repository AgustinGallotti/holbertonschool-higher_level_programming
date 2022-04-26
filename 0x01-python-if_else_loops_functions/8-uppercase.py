#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
    if (97 >= c < 122):
        i = ord(i - 32)
        i = chr(i)
    print(f"{c}", end='')
