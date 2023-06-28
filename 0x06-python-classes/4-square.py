#!/usr/bin/python3
"""Defining a square class"""


class Square:
    """The body of the class"""

    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
        def area(self):
            return int(self.__size) ** 2
