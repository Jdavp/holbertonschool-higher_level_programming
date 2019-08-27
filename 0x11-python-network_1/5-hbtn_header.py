#!/usr/bin/python3
'request to the URL and displays the value of the variable X-Request-Id'
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://intranet.hbtn.io/status')
    print(r.headers.get('X-Request-Id'))
