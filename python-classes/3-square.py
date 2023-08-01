#!/usr/bin/python3
"""
This module calculates the area of a square.
"""
class Square:
    """
    A class that defines a square.
    Attributes:
        size (int): The size of thr square
    """
    def __init__(self, size=0):
        self.__size = size
    """
    Set the value of the size 
    """
    @property
    """
    sets the value
    """
    def size(self):
        return self.__size
    """
    size.setter: sets and validate the value of the size
    """
    @size.setter
    """
    method:
        size: validates the value of the size
    """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    method:
        area: calculates the area of the square.
    """
    def area(self):
        return self.__size * self.__size
