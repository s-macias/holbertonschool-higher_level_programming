#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
import urllib.requests
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: <class 'bytes'>")
    print("\t- content: b'OK'")
    print("\t- utf8 content: OK")
