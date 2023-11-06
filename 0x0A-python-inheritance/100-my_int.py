#!/usr/bin/python3
"""> " Module doc " <"""


class MyInt(int):
    """class"""

    def __eq__(self, other):
        """__eq__"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """__ne__"""
        return not super().__ne__(other)
