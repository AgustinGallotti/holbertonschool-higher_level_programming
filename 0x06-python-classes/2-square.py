#!/usr/bin/python3
class Square:
    __size = None #private class of my size
    try type(size) == int:
        def __init__(self, size=0): #new class
        self.__size=size
    except type(size) != int:
            print(TypeError, "size must be an integer\n")
    except (size < 0):
        print(TypeError, "size must be >= 0\n")
