#!/usr/bin/python3
"""Rectangle inheret geo"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Constructor for Rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
