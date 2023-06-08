#!/usr/bin/python3

def lookup(obj):
    list = []
    obj_atrributes = obj.__dict__.keys()
    for obj_attribute in obj_atrributes:
        list.append(obj_attribute)
    return list
