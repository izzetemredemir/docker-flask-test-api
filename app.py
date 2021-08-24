from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def Main():
    return 'Hello World'

@app.route('/api/list/', methods=['GET'])
def GetAll():
    if request.method == "GET":

        return 'Get Request Working...'

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")