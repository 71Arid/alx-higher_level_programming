#!/usr/bin/python3
"""Module Mylist"""


class Mylist(list):
    """ inherits from list"""

    def print_sorted(self):
        """ prints sorted list"""

        print(sorted(self))
