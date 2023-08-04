"""
An Empty class.
"""

class BaseMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseMetaClass):
    """
    Do nothing: By passing pass.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    

print(dir(BaseGeometry))