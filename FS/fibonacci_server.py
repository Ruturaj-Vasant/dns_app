# Ruturaj Vasant Tambe DCN Lab 3 N10333254
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Simple Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Register endpoint
@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')

    if not hostname or not ip or not as_ip or not as_port:
        return jsonify({'error': 'Missing parameters'}), 400

    # Here you would typically send the registration to the AS via UDP
    # This is simplified for illustration purposes
    print(f"Registered {hostname} with IP {ip} to AS {as_ip}:{as_port}")
    return jsonify({'message': 'Registration successful'}), 201

# Fibonacci endpoint
@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get('number')
    if number is None or not number.isdigit():
        return jsonify({'error': 'Invalid input'}), 400
    
    number = int(number)
    result = fibonacci(number)
    return jsonify({'fibonacci': result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)