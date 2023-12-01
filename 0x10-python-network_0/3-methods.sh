#!/bin/bash
# Displays all HTTP methods the server will accept for a specified URL using curl.
curl -sI "$1" | grep -i Allow | sed 's/Allow: //' | tr -d '\r'
