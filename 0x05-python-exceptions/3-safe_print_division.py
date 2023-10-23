#!/usr/bin/python3
def safe_print_division(a, b):
    try :
        r = a / b
    except ZeroDivisionError:
        r = None
    print("Inside result: {}".format(r))
