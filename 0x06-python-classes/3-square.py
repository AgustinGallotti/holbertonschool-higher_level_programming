#!/usr/bin/python3
class Square:
    """type of class private"""
    __size = None
    """define my class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """finally realize my task"""
            self.__size = size
    """ defien other module """
    def area(self):
        """define my function in only one line, without self"""
        return self.__size ** 2
        """return my function in pow of two"""
