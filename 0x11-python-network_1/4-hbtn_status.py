#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response in a specific format.
"""

import requests

def hbtn_status():
    """
    Fetches https://alx-intranet.hbtn.io/status and displays the body of the response.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

if __name__ == "__main__":
    hbtn_status()
