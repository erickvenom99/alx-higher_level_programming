#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    resp = requests.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
