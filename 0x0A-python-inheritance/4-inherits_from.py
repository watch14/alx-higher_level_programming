#!/usr/bin/python3
"""inheret from *"""


def inherits_from(obj, a_class):
    """obj inheret from a_class"""
    return issubclass(type(obj), a_class)
