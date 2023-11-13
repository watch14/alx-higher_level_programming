#!/usr/bin/python3
"""Base"""
import json


class Base:
    """base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json to file"""
        if list_objs is not None:
            list_objs = [k.to_dictionary() for k in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """list of JSON"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            rs = Rectangle(1, 1)
        elif cls is Square:
            rs = Square(1)
        else:
            rs = None
        rs.update(**dictionary)
        return rs

    @classmethod
    def load_from_file(cls):
        """json.load no s"""
        from os import path
        file = f"{cls.__name__}.json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
