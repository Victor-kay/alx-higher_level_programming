#!/bin/bash
# Script: get_size.sh
# Description: Fetches a URL using curl, extracts the size of the response body in bytes.

curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r'
