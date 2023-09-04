#!/usr/bin/python3

"""
Module: 1-rectangle
This is the "1-rectangle" module.
The 1-rectangle module supplies one class, Rectangle.
"""

class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for width attribute.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        Args:
            value (int): The new width value.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.
        Args:
            value (int): The new height value.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
