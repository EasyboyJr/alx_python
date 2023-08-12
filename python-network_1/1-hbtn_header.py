"""
A python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)
    
url = sys.argv[1]
    
try:
    response = requests.get(url)
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
             print("X-Request-Id not found in the response header.")
    else:
         print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")