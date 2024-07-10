#!/usr/bin/python3
"""Python script takes in a URL and  email address"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
