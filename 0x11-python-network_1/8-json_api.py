#!/usr/bin/python3
"""Send POST request with letter as parameter"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        param = {'q': sys.argv[1]}
    else:
        param = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=param)
    if r.json():
        uid = r.get('id')
        name = r.get('name')
        print("[{}] {}".format(uid, name))
    elif r.json() == {}:
        print("No result")
    else:
        print("Not a valid JSON")
