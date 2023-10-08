#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = [my_list[i] for i in range(len(my_list)) if i != idx]
    return new
