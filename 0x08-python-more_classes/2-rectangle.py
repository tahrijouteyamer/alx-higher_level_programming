#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """The ectangle class body"""

    def __init__(self, width=0, height=0):
        """It initializes a Rectangle width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """It retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """It sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """It calculates the area of a Rectangle instance
        Returns:
            An area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """It calculates the perimeter of a Rectangle instance
        Returns:
            The perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
