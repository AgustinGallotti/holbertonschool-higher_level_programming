#!/usr/bin/python3
"""
    module
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    repo = argv[1]
    owner = argv[2]
    api = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    r = requests.get(api)
    listt = r.json()
    if r.status_code == 200:
        for i in listt[:10]:
            sha = i.get('sha')
            author = i.get("commit").get("owner").get("name")
            print("{}: {}".format(sha, author))
