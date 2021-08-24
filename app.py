from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def Main():
    return 'Hello World'

@app.route('/api/list/', methods=['GET'])
def ApiList():
    if request.method == "GET":
        parm = request.args.get('parm')
        return 'Get Request Working... param='+parm

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")