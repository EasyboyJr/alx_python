"""
An Empty class.
"""


class BaseGeometry:
    """
    Do nothing: By passing pass.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']