from mongo_db_update import insert_into_db
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
    insert_into_db(js['uuid'],js['url'],js['Topics'],js['voice'])
    print("succesfully handled ")
    return  'ok\n'

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=3000,
        debug=True
    )