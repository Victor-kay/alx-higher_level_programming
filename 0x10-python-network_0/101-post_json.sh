#!/bin/bash
# Sends a JSON POST request to the provided URL with the contents of the specified file and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
