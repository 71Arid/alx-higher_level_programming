#!/usr/bin/python3
""" Base Geometry object """


class BaseGeometry:
    """empty class"""

    def area(self):
        """ area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates an integer """
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
