from flask import Flask, jsonify
from flask_cors import CORS
from rate_limiter import SlidingWindowCounter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address
)

window_size = 60  # 1 minute
limit = 100  # 100 requests per minute

CORS(app)

limiter_counter = SlidingWindowCounter(window_size, limit)

# Define rate limit rule using the sliding window counter


@limiter.request_filter
def sliding_window_rate_limit():
    limiter_counter.add_request()
    return limiter_counter.is_allowed()


@app.route('/')
def hello():
    return jsonify(message='Hello, this is your API!')


@app.route('/GetOrderInformation')
def getOrder():
    if limiter_counter.is_allowed():
        return jsonify(message='GetOrderInformation')
    else:
        return jsonify(error='Rate limit exceeded'), 429


@app.route('/RequestOrderInvoices')
def requestOrderInvoices():
    if limiter_counter.is_allowed():
        return jsonify(message='RequestOrderInvoices')
    else:
        return jsonify(error='Rate limit exceeded'), 429


@app.route('/CreateOrder', methods=['POST'])
def createOrder():
    if limiter_counter.is_allowed():
        return jsonify(message='CreateOrder')
    else:
        return jsonify(error='Rate limit exceeded'), 429


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
