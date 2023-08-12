"""
A script that takes in a URL, sends a request to the URL and displays the body of the response.
"""
import requests
import sys

def main():
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(f"Response body:\n{response.text}")

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
