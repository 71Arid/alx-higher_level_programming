#!/usr/bin/python3
""" same object """


def inherits_from(obj, a_class):
    """ checks for same class"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
