import requests
import json

def send_file(url):
    with open('config.txt','r') as inf:
        payload= eval(inf.read())
    print(payload)
    r=requests.post(url,data=json.dumps(payload))
    print(r.text)