#!/bin/bash
# Sends a GET request to a specified URL using curl and displays the body of the response for a 200 status code.
curl -s -w "%{http_code}" "$1" | awk '/200/{getline; print}'
