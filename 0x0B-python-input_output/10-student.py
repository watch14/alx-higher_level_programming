#!/usr/bin/python3
"""class student"""


class Student:
    """student info"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for at in attrs:
                if type(at) in not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        info = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                info[key] = value
        return info
