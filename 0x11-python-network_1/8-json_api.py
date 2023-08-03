#!/usr/bin/python3
"""
This script sends a POST request to the web server at
http://0.0.0.0:5000/search_user with a letter as a parameter.
The letter is passed as an argument when running the script.
If no argument is provided, the letter is set to an empty string ('').
The response from the server is expected to be a JSON object.
If the JSON object is properly formatted and not empty, the script prints
the id and name as [<id>] <name>.
If the JSON object is invalid, the script prints "Not a valid JSON".
If the JSON object is empty, the script prints "No result".

Usage: python <script_name> [<letter>]

Arguments:
<letter> (optional) : A letter to be used as the 'q' parameter in
the POST request.

Example usage:
    $ python script.py
    No result

    $ python script.py a
    [8446] amnirqhtfjq

    $ python script.py 2
    No result

    $ python script.py b
    [7094] bmofakakhke

Dependencies:
    - Python 3
    - requests package
    (This script uses the 'requests' library to make HTTP requests.)

Note: The JSON responses from the server are randomly generated.
"""

import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': letter}
    resp = requests.post(url, data=values)
    try:
        data = resp.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
