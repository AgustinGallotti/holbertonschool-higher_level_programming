#!/usr/bin/python3
"""
    module
"""

if __name__ == '__main__':
    import requests
    import sys

    q = {"[id]": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, q)
    print(r)
    print(r.json())
