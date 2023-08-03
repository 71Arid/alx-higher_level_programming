#!/usr/bin/python3
"""
7-error_code.py

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
import requests

if __name__ == "__main__":
    url = str(sys.argv[1])
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code:", e.response.status_code)
