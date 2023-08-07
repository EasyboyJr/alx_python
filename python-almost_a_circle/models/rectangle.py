'''
Rectangle class: inherits from base class
'''
from models.base import Base


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
        self.__width = new_width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        self.__x = new_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y):
        self.__y = new_y