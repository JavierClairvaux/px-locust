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
        j = {
            'pid': db.get('pid'),
            'running': db.get('running')
                }
        return jsonify(j)
    content = request.get_json()
    proc = subprocess.Popen(["locust", "-r", content["hrate"], "-u", content["users"], "-f", "/locust/locustfile.py", "-H", os.environ['FRONTEND_ADDR'], "--headless"] )
    db.set('running', True)
    db.set('pid', proc.pid)
    j = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return jsonify(j)

@app.route('/invokust', methods = ['DELETE'])
def stopLocust():
    if not db.get('running'):
        j = {
            'pid': db.get('pid'),
            'running': db.get('running')
                }
        return jsonify(j)

    os.kill(db.get('pid'), signal.SIGTERM)
    db.set('running', False)
    db.set('pid', 0)
    j = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return jsonify(j)

@app.route('/invokust', methods = ['GET'])
def getLocust():
    j = {
        'pid': db.get('pid'),
        'running': db.get('running')
            }
    return jsonify(j)

app.run(host='0.0.0.0')

