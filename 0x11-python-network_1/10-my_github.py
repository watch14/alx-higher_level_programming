#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys

if __name__ == "__main__":
    url = "https://github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=auth)

    data = res.json()
    if data:
        print(data["id"])
    else:
        print("None")
