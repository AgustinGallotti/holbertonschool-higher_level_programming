#!/usr/bin/python3
"""define my class"""


class Square:
    """my instance of size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position mus be a tuple of 2 positive integers")
            """finally realize my task"""
        self.__position = position
        self.__size = size

    def area(self):
        """define my function in only one line, without self"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retnr size of the square"""
        return self._size

    @property
    def position(self):
        """return the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 2 or value[1] < 2:
            raise TypeError(
               "position must be a tuple of 2 positive integers")
        self.__position = value
        

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """the size exist"""
        if self.__size == 0:
            print()
        else:
            """run for print my square"""
            for i in range(self.__position[1]):
                print()
            num = '#' * self.__size
            none = ' ' * self.__position[0]
            for i in range(self.__size):
                """print my square"""
                print(none, num, sep="")