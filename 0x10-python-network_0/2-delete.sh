#!/usr/bin/python3
"""
This script sends a DELETE request to the URL passed as the first argument
and displays the body of the response.
"""

import sys
import requests

def delete_request(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    response = requests.delete(url)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    delete_request(url)
