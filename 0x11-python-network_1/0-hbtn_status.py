#!/usr/bin/python3
"""A Python script that
   - fetches the URL
   - displays the body in tabulation
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as req:
        content = req.read()
        print('Body response:')
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
