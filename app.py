from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Project: Cloud-Native Flask Portfolio</h1><p>Status: Running in Docker!</p>"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)