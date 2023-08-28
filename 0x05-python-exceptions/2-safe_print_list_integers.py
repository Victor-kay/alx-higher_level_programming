#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in a list.

    Args:
        my_list (list): The list to extract integers from.
        x (int): The number of integers to print.

    Returns:
        The number of integers printed.
    """
    printed_count = 0
    index = 0

    while printed_count < x and index < len(my_list):
        try:
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                printed_count += 1
        except IndexError:
            break
        index += 1

    print()  # Print a newline after all integers have been printed
    return printed_count
