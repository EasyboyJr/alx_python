"""
An Empty class.
"""


class BaseGeometry:
    """
    Do nothing: By passing pass.
    """
    def __dir__(self):
        attributes = super().__dir__()
        return [i for i in attributes if i != '__init_subclass__']
