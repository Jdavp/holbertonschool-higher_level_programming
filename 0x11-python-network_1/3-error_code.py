#!/usr/bin/python3
'takes in a URL and an email, sends a POST request to the passed URL'
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode('utf-8'))
