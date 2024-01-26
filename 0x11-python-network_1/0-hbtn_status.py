#!/usr/bin/python3
""" fetches status """
import urllib.request

if __name__ == "__main__":
    requ = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(requ) as res:
        cont = res.read()
        print("Body response:")
        print(f"\t- type: {type(cont)}")
        print(f"\t- content: {cont}")
        print(f"\t- utf8 content: {cont.decode('utf-8')}")
