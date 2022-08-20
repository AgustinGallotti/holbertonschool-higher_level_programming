#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    commits = 'https://developer.github.com/v3/repos/commits/'
    repo = argv[1]
    owner = argv[2]
    r = requests.get(commits, commit=(repo, owner))
    check = r.json()
    try:
        print(check['author name'])
    except no_user:
        print("No user")
