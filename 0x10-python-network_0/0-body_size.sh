#!/bin/bash
# Script: get_size.sh
# Description: Fetches a URL using curl, extracts the size of the response body in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Fetch the URL using curl in silent mode and store the response in a variable
response=$(curl -sI "$1")

# Extract the Content-Length header from the response
content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')

# Check if Content-Length is present in the response
if [ -z "$content_length" ]; then
    echo "Error: Content-Length not found in the response headers"
    exit 1
fi

# Display the size in bytes
echo "Size of the response body: ${content_length} bytes"
