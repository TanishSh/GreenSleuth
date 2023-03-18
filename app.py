from flask import Flask, request
import flask
import os
import librosa
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload')
def hello_world():
    # Get files with wav suffix
    files = [os.path.join("../../../../",f) for f in os.listdir('../') if f.endswith('.wav')]
    print(files)

    return flask.jsonify({"data": "hello"})

if __name__ == '__main__':
    app.run()