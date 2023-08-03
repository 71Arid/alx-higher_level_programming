#!/usr/bin/python3
"""
3-error_code.py

This script sends a GET request to a specified URL and handles HTTP errors.

Usage: python3 3-error_code.py <url>

Arguments:
    <url> - The URL to send the GET request.

Example:
    python3 3-error_code.py http://0.0.0.0:5000/doesnt_exist

Output:
    The script will print the data received from the server if
    the request is successful.
    If the server returns an HTTP error, the script will print the error code.

Note:
    This script uses the 'urllib.request' module to send the GET request.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = str(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as r:
            data = r.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
