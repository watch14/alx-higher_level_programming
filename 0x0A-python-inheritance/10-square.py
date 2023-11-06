#!/usr/bin/python3
"""Square inherits Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        super().__init__(size, size)

    def area():
        return self.__width * self.__height
