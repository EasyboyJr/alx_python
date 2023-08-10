import requests
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()

