import sys
import requests

def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Request failed with status code: []")