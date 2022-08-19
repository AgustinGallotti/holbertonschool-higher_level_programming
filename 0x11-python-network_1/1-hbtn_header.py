#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.urlopen(url)
    with req as response:
        print(response.headers.get('X-Request-Id'))
