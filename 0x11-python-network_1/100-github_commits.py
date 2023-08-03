#!/usr/bin/python3
"""
"""

import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[1]
    repository = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
