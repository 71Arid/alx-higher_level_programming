#!/usr/bin/python3
"""
6-post_email.py

This script sends a POST request to a specified URL with an email parameter.
The email parameter is provided as a command-line argument
when running the script.

Usage: python3 2-post_email.py <base_url> <email>

Arguments:
    <base_url> - The base URL where the POST request will be sent.
    <email>    - The email address that will be included in the POST request.

Example:
python3 2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

Output:
    The script will print the response received from the server, which should
    contain the email address provided in the POST request.

Note:
    This script uses the 'urllib.request' module
    to send the POST request, and it assumes
    that the server at the specified URL will
    correctly handle the request and respond
    with the appropriate data.
"""

import sys
import requests

if __name__ == "__main__":
    values = {'email': str(sys.argv[2])}
    r = requests.post(sys.argv[1], data=values)
    print(r.text)
