#!/usr/bin/python3
""" Define add fuction """


def add_integer(a, b=98):
    """ Returns int addition """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
