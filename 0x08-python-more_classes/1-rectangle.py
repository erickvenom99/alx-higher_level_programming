#!/usr/bin/python3
"""Module for defining a rectangle class."""


class Rectangle:
    """A class to represent a rectangle.

    Attributes:
        __width (int): The width of the rectangle, defaults to 0.
        __height (int): The height of the rectangle, defaults to 0.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Get or set the height of the Rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
