"""
A python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

url = sys.argv[1]
req = requests.get(url)
r = req.headers['X-Requests-Id']
print(r)