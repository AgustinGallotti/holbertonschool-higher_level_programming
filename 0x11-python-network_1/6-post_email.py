#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests
    import sys

    r = requests.post(sys.argv[1])
    print(r.text, sys.argv[2])
