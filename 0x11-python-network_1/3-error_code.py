#!/usr/bin/python3
"""Python script that takes in a URL,
   sends a request to the URL
   displays the body of the response (decoded in utf-8)
   manage urllib.error.HTTPError exceptions
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
