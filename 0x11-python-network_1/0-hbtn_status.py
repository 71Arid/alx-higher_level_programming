#!/usr/bin/python3
""" module to display status code """

import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as r:
    data = r.read()

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
print("\t- utf8 content: {}".format(data.decode('utf-8')))
