#!/bin/bash
# script to display status code without response content
curl -s -o /dev/null -w "%{http_code}" "$1"
