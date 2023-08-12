#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage:  <URL>
"""
"""Takes URL, sends a request and displays the value of X-Request-Id"""
import requests
import sys

def main():
    url=sys.argv[1]
    r= requests.get(url)
    if'X-Request-Id'in r.headers:
        r1=r.headers['X-Request-Id']
        print(r1)
    else:
        print("None")
if __name__ == '__main__':
    main()
