#!/usr/bin/python3
class Square:
    __size = None #private class of my size
    def __init__(self, size=0): #new class
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size=size
