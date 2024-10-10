# Ruturaj Vasant Tambe DCN Lab 3 N10333254
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    # Extract query parameters
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # Validate parameters
    if not all([hostname, fs_port, number, as_ip, as_port]):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify({"error": "Invalid number parameter"}), 400

    # Query the Authoritative Server (AS) for the IP address of the Fibonacci Server (FS)
    response = requests.get(f"http://{as_ip}:{as_port}/query?name={hostname}")

    if response.status_code == 200:
        ip_address = response.json()["IP"]
        # Request the Fibonacci number from the Fibonacci Server (FS)
        fs_url = f"http://{ip_address}:{fs_port}/fibonacci?number={number}"
        fs_response = requests.get(fs_url)

        if fs_response.status_code == 200:
            return fs_response.json(), 200
        else:
            return jsonify({"error": "Error retrieving Fibonacci number"}), fs_response.status_code
    else:
        return jsonify({"error": "DNS query failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)