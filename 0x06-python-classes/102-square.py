#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size (float or int, optional): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator."""
        return self.area() <= other.area()

if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(4)

    print("Area of square1:", square1.area())
    print("Area of square2:", square2.area())

    print("square1 == square2:", square1 == square2)
    print("square1 != square2:", square1 != square2)
    print("square1 > square2:", square1 > square2)
    print("square1 >= square2:", square1 >= square2)
    print("square1 < square2:", square1 < square2)
    print("square1 <= square2:", square1 <= square2)
