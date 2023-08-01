#!/usr/bin/python3
"""
A module that calculate the area of a square.
Methods:
    __init__: initialises the object
    __validate_size: Validates the size
    area: Calculate the area of a square
"""
class Square:
    """
    A class that define a square.
    Attributes:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        """
        Attributes:
            self.__size: sets the value of thr size.
        """
        self.__size = size
        self.__validate_size()
    """
    A method that validate the size.
    checks if it is an integer and if it is greater or equal to zero
    """
    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
    """
    A method that calculates the area of the square.
    """
    def area(self):
        return self.__size * self.__size
