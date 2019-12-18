from flask import Flask
from flask import jsonify
from GetProxyFromRedis import *
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get')
def get():
    return jsonify(get_one())


@app.route('/get_nums')
def getNum():
    return jsonify(get_nums())


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    # http://xx.xx.xx.xx:9999
    delete_one(proxy.split("//")[-1])
    return jsonify({"code": 0, "src": "success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
