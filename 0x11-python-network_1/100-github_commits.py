#!/usr/bin/python3
"""A python script that takes two arguments and
    prints 10 commits from most recent to
    oldest
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print(f"{sha}:{author}")
    except IndexError:
        pass
