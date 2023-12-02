#!/usr/bin/python3
"""
This script takes in a repository name and owner name, and
uses the GitHub API to fetch and print the 10 most recent commits.
"""

import requests
import sys

def get_github_commits(repository, owner):
    """
    Takes a repository name and owner name, uses the GitHub API
    to fetch and print the 10 most recent commits.
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Error: Unable to fetch commits.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    get_github_commits(repository, owner)
