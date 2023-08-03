#!/usr/bin/python3
"""
A class BaseGeometry
Method:
    area: Raises an exeption.
"""


class BaseGeometry:
    """
    Do nothing: By passing pass.
    """
    def __dir__(self):
        attributes = super().__dir__()
        return [i for i in attributes if i != '__init_subclass__']
    """
    area: takes in no agument other than self.
    """
    def area(self):
        """
        Raises an exception.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        validates the input.
        Attributes:
            name(string): the name string.
            value(int): must be an integer greater than 0.
        """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name)
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            

class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        attributes:
            width: int
            height: int
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
