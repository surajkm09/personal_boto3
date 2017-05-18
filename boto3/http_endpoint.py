from flask import Flask, request
import requests
import json
from play_text import play_text
from intial_arn_setup import intial_arn_finder

app = Flask(__name__)

def msg_process(msg, tstamp):

    # do stuff here, like calling your favorite SMS gateway API
    with open('config.txt', 'r') as inf:
        dict_from_file = eval(inf.read())
    status=str(dict_from_file['voice'])
    if status == 'on':
        play_text(msg)

@app.route('/', methods = ['GET', 'POST', 'PUT'])
def sns():
    # AWS sends JSON with text/plain mimetype
    js = ""
    try:
        js = json.loads(request.data.decode('utf-8'))
    except:
        pass

    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    # subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])

    if hdr == 'Notification':

        msg_process(js['Message'], js['Timestamp'])

    return 'OK\n'

if __name__ == '__main__':
    app.run(
        host = "127.0.0.1",
        port = 5000,
        debug = True
    )