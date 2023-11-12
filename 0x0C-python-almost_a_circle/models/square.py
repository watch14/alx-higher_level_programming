#!/usr/bin/python3
"""SQUARE"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns square."""
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__, self.id, self.x, self.y, self.size)

    def __update(self, id=None, size=None, x=None, y=None):
        """updates attr"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
