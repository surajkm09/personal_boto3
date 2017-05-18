from monogo_db_update import insert_into_db
from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST', 'PUT'])
def handle_requests():
    js = ""
    try:
        js = json.loads(request.data.decode('utf-8'))
    except:
        pass
    insert_into_db(js['uuid'],js['url'],js['topics'])
    print("succesfully handled ")
    return  'ok\n'

def launch_app():
    app.run(
        host="127.0.0.1",
        port=3000,
        debug=True
    )