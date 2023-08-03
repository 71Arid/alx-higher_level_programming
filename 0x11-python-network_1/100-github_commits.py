#!/usr/bin/python3
"""
This script fetches the last 10 commits from a specified
GitHub repository using the GitHub API.
The GitHub repository is specified by the
owner's name and the repository's name as command-line arguments.

Usage: python script.py <owner_name> <repository_name>

Arguments:
<owner_name> (required): The name of the owner/organization
of the GitHub repository.
<repository_name> (required): The name of the GitHub repository.

Example usage:
    $ python script.py rails rails
    3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
    f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
    bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
    f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
    0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
    24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
    668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
    a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
    28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
    8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França

Dependencies:
    - Python 3
    - requests package
    (This script uses the 'requests' library to make HTTP requests.)

Note: The script uses the GitHub API to fetch the
last 10 commits from the specified repository and owner.
The fetched commits are then printed with
their corresponding SHA and author names.
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
