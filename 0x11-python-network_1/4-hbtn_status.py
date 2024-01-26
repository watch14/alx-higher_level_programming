#!/usr/bin/python3
"""Fetches arg.1"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        cont = res.read().decode("utf-8")
        print(f"Body response:")
        print(f"\t- type: {type(cont)}")
        print(f"\t- content: {cont}")
