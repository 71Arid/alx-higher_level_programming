#!/usr/bin/python3
"""
This script fetches the GitHub user ID using the GitHub API
with Basic Authentication using a personal access token.
The script expects two command-line arguments: the GitHub username
and the personal access token.

Usage: python script.py <username> <personal_access_token>

Arguments:
<username> (required): The GitHub username of the user.
<personal_access_token> (required): The personal access token
used for authentication.

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
