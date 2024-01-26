#!/usr/bin/python3
""" fetches status """
import urllib.request

requ = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(requ) as res:
    cont = res.read()
    print("Body response:")
    print(f"    - type: {type(cont)}")
    print(f"    - content: {cont}")
    print(f"    - utf8 content: {cont.decode('utf-8')}")
