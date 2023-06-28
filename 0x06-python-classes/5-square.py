#!/usr/bin/python3
"""Defination of a square class"""


class Square:
    """The body of the class"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return int(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
