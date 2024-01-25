#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
    sorted_list = sorted(list_of_integers)
    return sorted_list[-1]
