#!/usr/bin/python3
""" REQUESTS - github API """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    request = requests.get(url, auth=auth)
    print(request.json().get("id"))
