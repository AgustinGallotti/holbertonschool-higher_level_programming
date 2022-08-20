#!/usr/bin/python3
"""
    module
"""

if __name__ == '__main__':
    import requests
    import sys
    if len(sys.argv) > 1:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ""}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, q)
    try:
        JS = r.json()
        if len(JS) == 0:
            print("No result")
        else:
            print("[{}] {}".format(JS["id"], JS["name"]))
    except Exception:
        print("Not a valid JSON")
