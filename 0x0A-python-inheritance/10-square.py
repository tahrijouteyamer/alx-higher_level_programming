#!/usr/bin/python3

"""Defines the Square module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class body."""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size
