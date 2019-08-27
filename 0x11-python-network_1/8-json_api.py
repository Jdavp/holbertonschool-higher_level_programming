#!/usr/bin/python3
'request to the URL and displays the body of the response (decoded in utf-8)'
if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'q': argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', payload)
    
    if r.raise_for_status():
        r.json()
