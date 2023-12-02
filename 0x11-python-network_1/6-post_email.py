#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response.
"""

import requests
import sys

def post_email(url, email):
    """
    Takes in a URL and an email address, sends a POST request to
    the passed URL with the email as a parameter, and displays
    the body of the response.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    post_email(url, email)
