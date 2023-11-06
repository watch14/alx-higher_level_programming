#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""
BaseGeometry = ___import___('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
