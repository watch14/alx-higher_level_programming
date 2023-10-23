#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as er:
        stderr.write("Exception: ", er)
        return False
