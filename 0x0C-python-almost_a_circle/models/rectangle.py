#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectange"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.raiser("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.raiser("height", value)
        self.__height = value

    @property
    def x(self):
        """ X """
        return self.__x

    @x.setter
    def x(self, value):
        self.raiser("x", value, False)
        self.__x = value

    @property
    def y(self):
        """ Y """
        return self.__y

    @y.setter
    def y(self, value):
        self.raiser("y", value, False)
        self.__y = value

    def raiser(self, name, value, ifeq=True):
        """the raiser"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if ifeq and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif not ifeq and value < 0:
            raise ValueError(f"{name} must be => 0")

    def area(self):
        """area"""
        return self.width * self.height

    def display(self):
        """ display with #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) "\
                f"{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, id=None, width=None, height=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
