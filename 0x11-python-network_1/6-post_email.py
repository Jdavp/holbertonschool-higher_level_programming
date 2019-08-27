#!/usr/bin/python3
'takes in a URL and an email, sends a POST request to the passed URL'
if __name__ == "__main__":
    import request
    from sys import argv

    payload = {'email': argv[2]}
    r = requests.post(argv[1], payload)
    print(r.text)
