#!/usr/bin/python3
"""writing a docstring"""
import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """ define magic """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """define area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ define circumference """
        return 2 * math.pi * self.__radius
