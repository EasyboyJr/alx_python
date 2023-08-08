"""
A square class: Inherits from the rectangle class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
     """
    A class representing a square.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
        x (int): The x-coordinate position of the square.
        y (int): The y-coordinate position of the square.
    """
     
     def __init__(self, size, x=0, y=0, id=None):
          """
        Initialize the square instance with specified attributes.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
            x (int, optional): The x-coordinate position of the square. Default is 0.
            y (int, optional): The y-coordinate position of the square. Default is 0.
            id (int, optional): The unique identifier. Inherits from Rectangle class.
        """
          super().__init__(size, size, x, y, id)
     @property
     def size(self):
         """Get the size of the square."""
         return self.width
     
     @size.setter
     def size (self, new_size):
        self.width = new_size
        self.height = new_size
    
     def __str__(self):
         """return the square in format."""
         return ("[Square] ({}) {}/{} - {}".format(id, self.x, self.y, self.width))