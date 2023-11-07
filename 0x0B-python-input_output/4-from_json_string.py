#!/usr/bin/python3
"""data structure json"""
import json


def from_json_string(my_str):
    """string to structure"""
    return json.loads(my_str)
