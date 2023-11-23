
from flask import Flask, jsonify, request
from flask_cors import CORS

from detect_person_page import detect_person_api

import sys
sys.executable

app = Flask(__name__)
app.register_blueprint(detect_person_api)
CORS(app, origins="*")


@app.route('/')
def home_page():
    str = '''

    <br><br> <b> Smart Room Data </b> <br><br>

    <br><br>

    '''

    return str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)