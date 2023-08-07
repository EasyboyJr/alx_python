'''
Base Module: this module contains the base class of all other classes in the project.
class:
    Base: created the base class.
'''


class Base:
    """
    Base class Method:
        __init__: Initialises the class with id(int),
                  Increment __nb_objects.
    Attributes:
        __nb_objects: Initial value = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Increments __nb_objects
        id(int): integer value.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects