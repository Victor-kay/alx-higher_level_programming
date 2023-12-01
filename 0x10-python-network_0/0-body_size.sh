#!/usr/bin/python3
"""
Script: get_size.py
Description: Fetches a URL using requests, extracts the size of the response body in bytes.
"""

import requests
import sys

response = requests.get(sys.argv[1])
print(len(response.content))
