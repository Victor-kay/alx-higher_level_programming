#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Example:
        >>> read_file("example.txt")  # Replace with the actual file name
        This is an example text file.
        It contains multiple lines.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

