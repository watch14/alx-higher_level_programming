#!/usr/bin/python3
"""
Base
"""


class base:
    """base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base__nb_objects
