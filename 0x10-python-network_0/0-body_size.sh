#!/bin/bash
# script to display content size of body
echo "$(curl -sI "$1")" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r'
