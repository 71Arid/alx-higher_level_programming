#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response.

Usage: python3 script_name.py URL

Parameters:
    - URL: The URL of the HTTP request to be sent.

Example:
    python3 script_name.py https://example.com
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
