from flask import Flask, jsonify
import os
    
app = Flask(__name__)
container_id = os.getenv("CONTAINER_ID", "unknown")

@app.route('/data')
def get_data():
    return jsonify({'data': 'This is some data!'})

@app.route('/')
def home_page():
    return jsonify({'data': f'Welcome from container {container_id}'})

@app.route('/text/<text>')
def add_page(text):
    return f'<h1>{text}</h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0')