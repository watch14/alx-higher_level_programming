#!/usr/bin/python3
""" REQUESTS - github API """
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://github.com/user"
    au = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=au)
    print(res.json().get("id"))
