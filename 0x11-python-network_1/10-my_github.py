#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and personal access token),
uses the GitHub API to display your id using Basic Authentication.
"""

import requests
import sys

def get_github_id(username, token):
    """
    Takes GitHub username and personal access token, uses Basic Authentication
    to access the GitHub API, and displays the user id.
    """
    url = "https://api.github.com/user"
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    get_github_id(username, token)
