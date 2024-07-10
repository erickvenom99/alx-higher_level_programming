#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
display the id and name like this: [<id>] <name>
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    param = {'q': letter}
    r = requests.post(url, data=param)

    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            get_id = resp.get("id")
            get_name = resp.get("name")
            print("[{}] {}".format(get_id, get_name))
    except ValueError:
        print("Not a valid JSON")
