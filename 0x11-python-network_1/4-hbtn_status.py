#!/usr/bin/python3
'fetches https://intranet.hbtn.io/status using request package'
if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("""Body response:"""'\n'
          '\t'"""- type: {}"""'\n'
          '\t'"""- content: {}"""'\n'
          .format(type(r.text), r.text))
