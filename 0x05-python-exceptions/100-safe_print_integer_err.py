#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        r = True
    except Exception as er:
        stderr.write("Exception: ", er, file=stderr)
        r = False
    return r
