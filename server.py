from flask import Flask
from flask import request
import subprocess
import os, signal
import pickledb

db = pickledb.load('process.db', False)
proc = None
app = Flask(__name__)
app.config["DEBUG"] = True
db.set('running', False)

@app.route('/', methods=['GET'])
def home():
        return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/invokust', methods = ['POST'])
def postJsonHandler():
    if db.get('running'):
        return '{"locust": "running"}'
    content = request.get_json()
    proc = subprocess.Popen(["locust", "-r", content["hrate"], "-u", content["users"], "-f", "/locust/locustfile.py", "-H", os.environ['FRONTEND_ADDR'], "--headless"] )
    db.set('running', True)
    db.set('pid', proc.pid)
    return '{"locust": "running"}'

@app.route('/invokust/stop', methods = ['GET'])
def stopLocust():
    if not db.get('running'):
        return '{"locust": "stopped"}'
    os.kill(db.get('pid'), signal.SIGTERM)
    db.set('running', False)
    return '{"locust": "stopped"}'

@app.route('/invokust/get', methods = ['GET'])
def getLocust():
    if db.get('running'):
        return '{"locust": "running"}'
    else:
        return '{"locust": "stopped"}'

app.run(host='0.0.0.0')

