#!/usr/bin/python3
"""Python script that takes a URL
   Displays the value of the X-Request-Id header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
