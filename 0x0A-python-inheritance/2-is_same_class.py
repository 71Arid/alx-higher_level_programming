#!/usr/bin/python3
""" same object """


def is_same_class(obj, a_class):
    """ checks for same class"""

    name = type(obj)
    if name == a_class:
        return True
    else:
        return False
