# Ruturaj Vasant Tambe DCN Lab 3 N10333254
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for registered domains
registered_domains = []

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    print("Received data:", data)  # Log the incoming data

    name = data.get('NAME')
    ip = data.get('IP')

    if not name or not ip:
        return jsonify({"error": "Invalid registration data"}), 400

    # Check if the domain is already registered
    for domain in registered_domains:
        if domain['name'] == name:
            return jsonify({"error": "Domain already registered"}), 400

    # Register the new domain
    registered_domains.append({'name': name, 'ip': ip})
    return jsonify({"message": "Registration successful"}), 200

@app.route('/query', methods=['GET'])
def query():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Name parameter is required"}), 400

    for domain in registered_domains:
        if domain['name'] == name:
            return jsonify(domain), 200

    return jsonify({"error": "Domain not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53533, debug=True)