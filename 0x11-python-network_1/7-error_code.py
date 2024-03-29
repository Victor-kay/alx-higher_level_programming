#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, displays the body
of the response, and prints an error message if the HTTP status code is
greater than or equal to 400.
"""

import requests
import sys

def fetch_url(url):
    """
    Takes in a URL, sends a request to the URL, displays the body
    of the response, and prints an error message if the HTTP status
    code is greater than or equal to 400.
    """
    response = requests.get(url)
    print(response.text)

    if response.status_code == 404:
        print(f"Error code: {response.status_code}")
        sys.exit(1)
    elif response.status_code >= 400:
        print(f"Error code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
