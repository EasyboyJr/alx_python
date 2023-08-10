"""
A python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

def main():
    """main function:checks for the url, if found, retrn thebx-id"""
    if len(sys.argv) != 2:
        print("Usage: 1-hbtn_header.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.statys_code == 200:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print("X-Request-Id: {}".format(x_request_id))
            else:
                print("X-Request-Id not found")
        else:
            print("Request failed with status code: {}".format(response.status_code))
    except requests.exeptions.RequestExeption as e:
        print("An error occured: {}".format(e))

if __name__ == "__main__":
    main()