#!/bin/bash
# This script sends a GET request to the given URL and displays the body of a 200 status code response

curl -s -w "%{http_code}" "$1" | awk 'BEGIN { body=0 } { if (body) print $0 } /^$/ { body=1 }' | tail -n 1
