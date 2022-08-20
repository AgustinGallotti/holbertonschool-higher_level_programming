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
    try:
        for check in range(10):
            print("{}: {}".format(
                listt[check].get("sha"),
                listt[check].get("commit").get("author").get("name")))
    except IndexError:
        pass
