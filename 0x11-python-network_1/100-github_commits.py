#!/usr/bin/python3
"""
"""
import requests
from sys import argv

if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    rest = requests.get(link)

    if "json" not in rest.headers.get('content-type'):
        print("Not a valid JSON")
    data = rest.json()
    values = 0
    for rest in data:
        if values > 9:
            break
        print(rest.get('sha') + ': ' +
              rest.get('commit').get('author').get('name'))
