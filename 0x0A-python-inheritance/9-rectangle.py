#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of a rectangle"""
        a = self.__width * self.__height
        return a

    def __str__(self):
        """str() representation of a rectangle"""
        rect = "[" + str(self.__class__.__name__) * "] "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect
