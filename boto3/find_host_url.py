import os
import json

def get_url():
    os.system("curl -s  http://localhost:4040/api/tunnels > tunnels.json",)
    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)
    msg=datajson['tunnels'][0]['public_url']
    return msg
if __name__ == '__main__':
    msg=get_url()
    print(msg)