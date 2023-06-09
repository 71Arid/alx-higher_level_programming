#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""
    
    def __int__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", __width)
        self.integer_validator("height", __height)
