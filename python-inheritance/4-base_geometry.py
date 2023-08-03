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
        raise Exception("area() is not implemented")
