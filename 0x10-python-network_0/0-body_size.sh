#!/usr/bin/env bash
# script to display content size of body
# Check if the URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
response=$(curl -sI "$url")
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

if [ -z "$content_length" ]; then
    echo "Error: Unable to get the Content-Length from the response."
    exit 1
fi

echo "${content_length}"
