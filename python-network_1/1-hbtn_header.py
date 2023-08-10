"""
A python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

def main():
    url = sys.argv[1]
    req = requests.get(url)
    r = req.headers['X-Requests-Id']
    if X-Request-Id is in req.headers:
        print(r)
    else:
        print("unable to fetch Id")

if __name__ =="__main__":
    main()
