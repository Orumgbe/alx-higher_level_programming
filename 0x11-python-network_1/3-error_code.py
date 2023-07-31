#!/usr/bin/python3
"""Script that takes url and displays body of the response"""

import sys
from urllib import request, error


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code ))
