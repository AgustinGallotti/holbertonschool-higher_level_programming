#!/usr/bin/python3
"""
    module
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    user = argv[1]
    passw = argv[2]
    response = requests.get('https://api.github.com/user', auth=(user, passw))
    data = response.json()
    try:
        print(data['id'])
    except Exception:
        print("None")
