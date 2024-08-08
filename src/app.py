from flask import Flask, jsonify, request

from placa import get_plate_number

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"

@app.route('/api/data', methods=['GET'])
def get_data():
    plate_number = get_plate_number("data/plate.jpg")
    data = {"plate_number": plate_number}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)