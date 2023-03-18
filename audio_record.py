import wave
import pyaudio

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# Initialize PyAudio
audio = pyaudio.PyAudio()

# Define constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Define global variables
frames = []
recording = False

@app.route('/_audio_record', methods=['POST'])
def start_recording():
    global recording
    if not recording:
        recording = True
        print("Starting recording...")
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        while recording:
            data = stream.read(CHUNK)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        print("Recording finished.")
        save_recording("recording.wav")
    else:
        recording = False
        print("Recording stopped.")
    return jsonify({'success': True})

def save_recording(filename):
    print("Saving recording to file...")
    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
    print("Recording saved to file:", filename)
    frames.clear()

if __name__ == '__main__':
    app.run(debug=True)
