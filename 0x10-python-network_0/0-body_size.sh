#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract URL from the command line arguments
url=$1

# Use curl to send a request and display the size of the response body in bytes
body_size=$(curl -sI "$url" | wc -c)

echo "Body size of $url: ${body_size} bytes"
