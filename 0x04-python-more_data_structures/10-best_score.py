#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    tmp = 0
    k = ""
    for key, value in a_dictionary.items():
        if value > tmp:
            tmp = value
            k = key
    return k   
