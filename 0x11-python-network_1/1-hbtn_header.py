#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found in the header of the response.

Usage: python3 script_name.py URL

Parameters:
    - URL: The URL of the HTTP request to be sent.

Example:
    python3 script_name.py https://example.com
"""

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(str(sys.argv[1])) as r:
        print(r.headers["X-Request-Id"])
