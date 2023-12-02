#!/usr/bin/python3
"""
This script sends a request to a specified URL and displays the body of the response.
It handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.
"""

import urllib.request
import urllib.error
import sys

def error_code(url):
    """
    Sends a request to the specified URL and displays the body of the response.
    Handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    error_code(url)
