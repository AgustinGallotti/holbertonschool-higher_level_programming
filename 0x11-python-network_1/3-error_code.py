#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from urllib.error import HTTPError
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            r_t = response.read()
            print(r_t.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
