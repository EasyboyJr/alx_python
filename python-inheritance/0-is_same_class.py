"""
A module that checks if an object is an instance of a class
"""
def is_same_class(obj, a_class):
    """
    Parameters:
        obj: The object.
        a_class: The class to be compared to.
    """
    value = type(obj) is a_class
    return value