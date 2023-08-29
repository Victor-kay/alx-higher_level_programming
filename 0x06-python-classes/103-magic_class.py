#!/usr/bin/python3
"""
This module defines the MagicClass class.
"""

import math

class MagicClass:
    """
    Represents a class with magic methods that match the provided bytecode behavior.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (float or int, optional): The radius of the circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
