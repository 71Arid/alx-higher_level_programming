#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp = {}
    for k, v in a_dictionary.items():
        cp[k] = v * 2
    return cp
