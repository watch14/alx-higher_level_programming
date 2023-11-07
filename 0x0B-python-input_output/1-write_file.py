#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """write text in file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
