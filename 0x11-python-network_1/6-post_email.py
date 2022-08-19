#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests
    import sys

    m = sys.argv[2]
    r = requests.post(sys.argv[1], m)
    print(r.text, m)
