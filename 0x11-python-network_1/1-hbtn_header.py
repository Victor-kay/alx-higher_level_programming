#!/usr/bin/python3
"""
This script sends a request to the given URL and displays the value of the X-Request-Id variable in the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        
        print(x_request_id)
