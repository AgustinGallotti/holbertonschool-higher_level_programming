#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r))
    print("\t- content:", r)
