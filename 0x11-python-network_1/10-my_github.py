#!/usr/bin/python3
"""
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    base_url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    response = requests.get(base_url, auth=auth)
    print(response.json().get("id"))
