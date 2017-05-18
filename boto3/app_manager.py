# manage.py
from flask import Flask


from flask_script import Manager, Server

from http_mongo_endpoint import run_mongo_endpoint

manager = Manager(app)

def crazy_call():
    print("crazy_call")

@manager.command
def runserver():
    run_mongo_endpoint()
    crazy_call()

if __name__ == "__main__":
    manager.run()