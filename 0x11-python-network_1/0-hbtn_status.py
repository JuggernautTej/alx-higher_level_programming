#!/usr/bin/python3
"""This """

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
print(body)
