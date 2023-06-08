#!/usr/bin/python3
""" same object """


def is_kind_of_class(obj, a_class):
    """ checks for same class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
