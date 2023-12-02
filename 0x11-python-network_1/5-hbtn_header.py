#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays
the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

def fetch_x_request_id(url):
    """
    Takes in a URL, sends a request to the URL, and displays
    the value of the variable X-Request-Id in the response header.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
