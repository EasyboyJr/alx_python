import requests
import sys

def send_post_request(url, letter):
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        response_json = response.json()
    except ValueError:
        # Invalid JSON response
        return None

    return response_json

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response_json = send_post_request(url, letter)

    if response_json is None:
        print("Not a valid JSON")
    elif isinstance(response_json, dict):
        if 'id' in response_json and 'name' in response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        elif 'message' in response_json:
            print(response_json['message'])
        else:
            print("No result")
    else:
        print("Not a valid JSON")
