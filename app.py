from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "IoT Sensor API Running!"})

@app.route('/sensor')
def sensor_data():
    return jsonify({"temperature": random.uniform(20, 40), "humidity": random.uniform(30, 80)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
