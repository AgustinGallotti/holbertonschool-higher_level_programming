#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    user = argv[1]
    passw = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, usr=(user, passw))
    access = r.json()
    try:
        print(access['id'])
    except Exception:
        print("None")
