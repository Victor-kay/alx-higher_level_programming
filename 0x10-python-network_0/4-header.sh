#!/bin/bash
# Sends a GET request to a specified URL with a custom header using curl.
curl -s -H "X-School-User-Id: 98" "$1"
