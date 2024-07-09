#!/usr/bin/python3
"""A Python script that
   sends a request to the URL and
   displays the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header_id = dict(response.headers).get("X-Request-Id")
        print(header_id)
