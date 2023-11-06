#!/usr/bin/python3
"""add_attribute"""


def add_attribute(class1, attribute, value):
    """Add attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(class1, attribute, value)
