"""
This module defines a square.
Methods:
    __init__: Initialises the object.
    __validate_size: validates the valie of the size
"""
class Square:
    """
    A class that defines a square.
    Attributes:
        size (int): the size of the square.
    """
    def __init__(self, size=0):
        """
        Attributes:
            self.__size: sets the value of the size.
        """
        self.__size = size
        self.__validate_size()
    
    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")