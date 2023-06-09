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
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of the rectangle."""
        return self.__size * self.__size
