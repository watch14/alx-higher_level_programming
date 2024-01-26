#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys

if __name__ == "__main__":
    user_repo = f"{sys.argv[2]}/{sys.argv[1]}"
    url = f"https://api.github.com/{user_repo}/commits"

    req = requests.get(url)
    data = req.json()

    for com in data:
        print(f"{com.get('sha')}: {\
                com.get('commit').get('author').get('name')}")
