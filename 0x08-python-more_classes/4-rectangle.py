#!/usr/bin/python3

"""Rectangle class."""


class Rectangle:
    """a rectangle."""

    def __init__(self, width=0, height=0):
        """a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the Rectangle width"""
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
        """Get the Rectangleheight"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle Area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Rectangle Parimeters"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rep = []
        for i in range(self.__height):
            [rep.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rep.append("\n")
        return ("".join(rep))

    def __repr__(self):
        """return a string representation of the rectangle"""
        rep = "Rectangle(" + str(self.__width)
        rep += ", " + str(self.__height) + ")"
        return (rep)
