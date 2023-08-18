#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())
    
    # Iterate through sorted keys and print key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

# Sample usage
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
