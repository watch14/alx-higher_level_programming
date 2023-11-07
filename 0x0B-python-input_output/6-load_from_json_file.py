#!/usr/bin/python3
"""load json file"""
import json


def load_from_json_file(filename):
    """load from .json"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
