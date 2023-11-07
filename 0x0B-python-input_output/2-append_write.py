#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append text in file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
