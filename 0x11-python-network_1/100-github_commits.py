#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys

if __name__ == "__main__":
    user_repo = sys.argv[2]"/"sys.argv[1]
    url = f"https://developer.github.com/{rep}/commits/"

    req = resuests.get(url)
    data = req.json()

    for com in data:
        print(f"{com.get('sha')}: {com.get('com').get('author').get('name')}")
