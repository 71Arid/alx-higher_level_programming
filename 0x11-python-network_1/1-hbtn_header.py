#!/usr/bin/python3
"""displays the value of the X-Request-Id variable 
found in the header of the response"""

import sys
import urllib.request

with urllib.request.urlopen(str(sys.argv[1])) as r:
    print(r.headers["X-Request-Id"])
