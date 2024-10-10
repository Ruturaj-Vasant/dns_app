# Ruturaj Vasant Tambe DCN Lab 3 N10333254
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to calculate Fibonacci number
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

# Fibonacci storage
fibonacci_numbers = {}

@app.route('/fibonacci/register', methods=['POST'])
def register_fibonacci():
    number = request.form.get('NUMBER')

    try:
        number = int(number)
        if number < 0:
            return jsonify({"error": "Invalid input"}), 400

        # Calculate and store Fibonacci number
        fib_value = fibonacci(number)
        fibonacci_numbers[number] = fib_value

        return jsonify({"message": "Fibonacci number registered successfully", "fibonacci": fib_value}), 200

    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get('number')
    
    if not number or not number.isdigit():
        return jsonify({'error': 'Invalid input'}), 400
    
    number = int(number)
    if number in fibonacci_numbers:
        return jsonify({'fibonacci': fibonacci_numbers[number]}), 200
    else:
        return jsonify({'error': 'Fibonacci number not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)