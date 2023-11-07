#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """UTF8 file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
