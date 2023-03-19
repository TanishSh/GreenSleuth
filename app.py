from flask import Flask, request
import flask
import os
import librosa
from flask_cors import CORS
import AItalk


app = Flask(__name__)
CORS(app)

@app.route('/upload')
def hello_world():
    # Get files with wav suffix
    #files = [os.path.join("../Downloads",f) for f in os.listdir('../Downloads') if f.endswith('.wav')]
    # filepath
    #files = "output.wav"
    # audioPath = files[-1]
    text =  AItalk.report()

    addressco, addressUrl = AItalk.address(text)

    print(addressco)
    print(addressUrl)
    return flask.jsonify({"coordinate": addressco, "map": addressUrl, "report": text})


if __name__ == '__main__':
    app.run()