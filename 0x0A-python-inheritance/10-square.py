#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('8-base_geometry').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Rectangle.

        Args:
            size (int): The size of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of the rectangle."""
        return self.__size * self.__size

    def __str__(self):
        """print() and str() representation"""
        st = "[" + str(self.__class__.__name__) + "] "
        st += str(self.__width) + "/" + str(self.__height)
        return st
