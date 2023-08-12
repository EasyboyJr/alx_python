

=======
#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage:  <URL>
"""
"""Takes URL, sends a request and displays the value of X-Request-Id"""
import requests
import sys

def main():
    url=sys.argv[1]
    email=sys.argv[2]
    r= requests.post(url, data={'email':email})
    r1=r.text
    print(r1)
if __name__ == '__main__':
    main()
