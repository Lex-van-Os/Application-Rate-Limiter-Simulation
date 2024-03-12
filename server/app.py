from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return jsonify(message='Hello, this is your API!')


@app.route('/GetOrderInformation')
def getOrder():
    return jsonify(message='GetOrderInformation')


@app.route('/RequestOrderInvoices')
def requestOrderInvoices():
    return jsonify(message='RequestOrderInvoices')


@app.route('/CreateOrder', methods=['POST'])
def createOrder():
    return jsonify(message='CreateOrder')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
