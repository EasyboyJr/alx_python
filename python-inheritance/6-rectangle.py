#!/usr/bin/python3
"""
A class BaseGeometry
Method:
    area: Raises an exeption.
"""
class BaseMetaClass(type):
    """
    overrides.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseMetaClass):
    """
    Do nothing: By passing pass.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
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
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""
Rectangle class.
Method:
    __init__: initialize.
"""
class Rectangle(BaseGeometry):
    """
    __init__: initialize
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
