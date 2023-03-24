#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ac = sorted(a_dictionary.keys())
    for i in ac:
        print(f"{i}: {a_dictionary[i]}")
