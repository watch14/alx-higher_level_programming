#!/usr/bin/python3
"""save to json"""
import json


def save_to_json_file(my_obj, filename):
    """save file .json"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, filename)
