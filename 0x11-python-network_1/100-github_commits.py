#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys

if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/"

    req = resuests.get(url)
    data = req.json()
    print(f"")
