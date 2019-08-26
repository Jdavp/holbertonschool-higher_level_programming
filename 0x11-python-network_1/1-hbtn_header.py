#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    headers = response.info()
    print(headers["X-Request-Id"])
