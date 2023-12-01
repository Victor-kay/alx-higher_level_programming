#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Set the URL and header variables
url="$1"
header="X-School-User-Id: 98"

# Send GET request using curl with the specified header
curl -H "$header" "$url"
