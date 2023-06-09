#!/usr/bin/python3
""" Base Geometry object """


class BaseGeometry:
    """empty class"""

    def area(self):
        """ area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates an integer """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
