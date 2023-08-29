#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square's sides.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance.

        Args:
            size (int, optional): The size of the square's sides.
            position (tuple, optional): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(val, int) for val in value) or
            not all(val >= 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        return self.my_print()

if __name__ == "__main__":
    mysquare = Square(3, (1, 2))
    print(mysquare)

    print("--")

    mysquare.size = 5
    print(mysquare)

    print("--")

    mysquare.position = (2, 1)
    print(mysquare)
