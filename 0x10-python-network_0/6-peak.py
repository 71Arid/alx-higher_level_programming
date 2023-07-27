#!/usr/bin/python3
# find peak function
def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
