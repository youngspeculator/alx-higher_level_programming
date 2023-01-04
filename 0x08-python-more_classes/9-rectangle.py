#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """ Represents the rectangle
        Attributes:
            number_of_instances (int): the number of rectangle instances
            print_symbol (str): ``#`` ie symbol used for string rep
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
            width(int): represents the width of the rectangle
            height(int): represents the height of the rectangle

        Returns:
            area(int):returns the rectangle area
            perimeter(int): returns the rectangle perimeter
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

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
        """ Returns the rectangle area.
            Area = height X length
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter
            Perimeter = (height + width) * 2
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area
           Args:
                rect_1: first rectangle
                rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a rectangle with width == height == size
        Args: size (int)
        """
        return (cls(size, size))

    def __str__(self):
        """Prints the rectangle with the character `#`"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
