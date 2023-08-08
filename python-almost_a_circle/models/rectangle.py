"""
Rectangle Class:
Inherits from Base class.
"""
from models.base import Base

class Rectangle(Base):
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate position of the rectangle.
        y (int): The y-coordinate position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance with specified attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position of the rectangle. Default is 0.
            y (int, optional): The y-coordinate position of the rectangle. Default is 0.
            id (int, optional): The unique identifier. Inherits from Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, new_width):
        """Set the width of the rectangle. Validates width."""
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width
    
    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, new_height):
        """Set the height of the rectangle. Validates height."""
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height
    
    @property
    def x(self):
        """Get the x-coordinate position of the rectangle."""
        return self.__x
    
    @x.setter
    def x(self, new_x):
        """Set the x-coordinate position of the rectangle. Validates x."""
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x
    
    @property
    def y(self):
        """Get the y-coordinate position of the rectangle."""
        return self.__y
    
    @y.setter
    def y(self, new_y):
        """Set the y-coordinate position of the rectangle. Validates y."""
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y
    
    def area(self):
        """Area method: returns width * height"""
        return self.__width * self.__height
    
    def display(self):
        """Display the rectangle using char #."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """Returns a formatted output."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))