#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        r = True
    except Exception as er:
        print("Exception: ", er, file=sys.stderr)
        r = False
    return r
