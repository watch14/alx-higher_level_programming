#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[:]
    if idx < 0 or idx >= len(new):
        return new_in_list
    new[idx] = element
    return new
