#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """A rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """It initializes  Rectangle instance in contructor.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width of a Rectangle instance
        Args:
            a value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """It retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """it sets the height of a Rectangle instance
        Args:
            the value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
