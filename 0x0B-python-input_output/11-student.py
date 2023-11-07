#!/usr/bin/python3
"""Class Student: Defines a Student class"""


class Student:
    """Student info"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to JSON"""
        if attrs is None:
            return self.__dict__

        info = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                info[key] = value
        return info

    def reload_from_json(self, json):
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
