#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """RECTANGLE CLASS"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
