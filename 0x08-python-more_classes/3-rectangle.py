#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents the rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
            width (int): represents the width of the rectangle
            height (int): represents the height of the rectangle

        Returns:
            area(int):returns the rectangle area
            perimeter(int): returns the rectangle perimeter
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self__.width
    

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area.Area = height X length"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter
        Perimeter = (height + width) * 2
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Prints the rectangle with the character ``#``"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return("".join(rec))
