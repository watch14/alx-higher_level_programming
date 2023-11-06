#!/usr/bin/python3
"""rectangle"""


class Rectangle(BaseGeometry):
    """rectange the inheret BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
