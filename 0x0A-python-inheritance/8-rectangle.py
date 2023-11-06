#!/usr/bin/python3
"""
rectangle
"""
BaseGeometry = ___import___('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectange the inheret BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
