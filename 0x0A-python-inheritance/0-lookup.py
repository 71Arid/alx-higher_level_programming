#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """finds attributes in dictionaries"""

    list = []
    obj_atrributes = obj.__dict__.keys()
    for obj_attribute in obj_atrributes:
        list.append(obj_attribute)
    return list
