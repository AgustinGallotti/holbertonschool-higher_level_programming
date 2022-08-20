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
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
