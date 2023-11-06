#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle inheret geo"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area():
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """retunr string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
