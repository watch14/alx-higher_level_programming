#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    r = True
    try:
        print("{:d}".format(value))
    except Exception as er:
        print("Exception: ", er, file=sys.stderr)
        r = False
    return r
