#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter,
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.parse

def post_email(url, email):
    """
    Sends a POST request to the given URL with the provided email parameter.
    Displays the body of the response (decoded in utf-8).

    :param url: The URL to send the POST request to.
    :param email: The email parameter to include in the request.
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

    print(f"Your email is: {email}.")
    post_email(url, email)
