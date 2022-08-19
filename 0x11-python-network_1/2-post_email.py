#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    P = {"email": sys.argv[2]}

    req = urllib.parse.urlencode(P)
    data = req.encode("ascii")

    with urllib.request.urlopen(sys.argv[1], data) as response:
        r_t = response.read()
        print(r_t.decode("utf-8"))
