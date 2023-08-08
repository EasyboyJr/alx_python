'''
Rectangle class: inherits from Base class
'''
from base import Base


class Rectangle(Base):
    """
    Rectangle class method:
        __innit__: initialises the class
        getters and setters
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        attributes :
            width
            height
            x
            y
        each with their own getters and setters.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        """
        Validates width
        """
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        """
        Validates height
        """
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        """
        Validates x
        """
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        if new_x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y):
        """
        Validates y
        """
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        if new_y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y