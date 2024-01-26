#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys

if __name__ == "__main__":
    url = "https://github.com/user"
    auth = (sys.argv[1], sys.argv[2])

    try:
        res = requests.get(url, auth=auth)
        res.raise_for_status()
        data = res.json()

        print(data["id"])

    except requests.exceptions.RequestException:
        print("None")
