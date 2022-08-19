#!/usr/bin/python3
"""module"""


if __name__ == '__main__':
    import urllib.request


    url = 'https://intranet.hbtn.io/status'
    status_code = urllib.request.urlopen(url)
    with status_code as response:
        status_code = response.read()
        print("Body response:")
        print("\t- type:", type(status_code))
        print("\t- content:", status_code)
        print("\t- utf8 content:", status_code.decode('utf-8'))
