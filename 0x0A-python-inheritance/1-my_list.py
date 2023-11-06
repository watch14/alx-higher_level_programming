#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """list"""
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
