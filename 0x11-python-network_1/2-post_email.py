#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter
and displays the body of the response.
"""

import urllib.parse
import urllib.request
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter
    and displays the body of the response.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    post_email(url, email)
