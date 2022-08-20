#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests
    from requests.exceptions import HTTPError
    import sys


    r = requests.get(sys.argv[1])
    if r:
        print(r.text)
    else:
        print("Error code:", r.status_code)
