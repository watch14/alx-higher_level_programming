#!/usr/bin/python3
"""saureas"""


class Square:
    """saqures"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                any(x < 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        square_str = ""
        if self.__size == 0:
            return square_str
        else:
            square_str += '\n' * self.__position[1]
            square_str += '\n'.join(
                    " " * self.__position[0] + "#" * self.__size
                    for _ in range(self.__size)
                    )
            return square_str
