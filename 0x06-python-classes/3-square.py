#!/usr/bin/python3
"""define my class"""


class Square:
    """private class"""
    __size = None
    """my instance of size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """finally realize my task"""
            self.__size = size

    def area(self):
        """define my function in only one line, without self"""
        return (self.__size ** 2)
