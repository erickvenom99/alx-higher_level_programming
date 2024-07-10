#!/usr/bin/python3
"""Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the email,
   and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_value = {'email': email}
    email_data = urllib.parse.urlencode(email_value).encode('ascii')

    request = urllib.request.Request(url, email_data)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
