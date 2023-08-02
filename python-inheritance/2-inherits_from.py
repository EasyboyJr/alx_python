"""
A function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""
def inherits_from(obj, a_class):
    """
    Parameters:
        obj: The object.
        a_class: The class.
    """
    return issubclass(type(obj), a_class)