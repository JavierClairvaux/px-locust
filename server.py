from flask import Flask, request, jsonify
import subprocess, os, signal, pickledb

db = pickledb.load('process.db', False)
proc = None
app = Flask(__name__)
app.config["DEBUG"] = True
db.set('running', False)

@app.route('/invokust', methods = ['POST'])
def postJsonHandler():
    if db.get('running'):
        res = {
            'pid': db.get('pid'),
            'running': db.get('running')
                }
        return ressonify(res)
    content = request.get_resson()
    proc = subprocess.Popen(["locust", "-r", content["hrate"], "-u", content["users"], "-f", "/locust/locustfile.py", "-H", os.environ['FRONTEND_ADDR'], "--headless"] )
    db.set('running', True)
    db.set('pid', proc.pid)
    res = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return ressonify(res)

@app.route('/invokust', methods = ['DELETE'])
def stopLocust():
    if not db.get('running'):
        res = {
            'pid': db.get('pid'),
            'running': db.get('running')
                }
        return ressonify(res)

    os.kill(db.get('pid'), signal.SIGTERM)
    db.set('running', False)
    db.set('pid', 0)
    res = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return ressonify(res)

@app.route('/invokust', methods = ['GET'])
def getLocust():
    res = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return ressonify(res)

app.run(host='0.0.0.0')

