#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))
