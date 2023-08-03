#!/usr/bin/python3
""" module to display status code """

import requests
url = "https://alx-intranet.hbtn.io/status"
data = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(data.text)))
print("\t- content: {}".format(data.text))
