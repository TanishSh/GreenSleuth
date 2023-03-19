import pyaudio
import wave
import numpy as np

# Custom function to calculate RMS value of audio data
def calculate_rms(audio_data):
    rms = np.sqrt(np.mean(np.square(audio_data)))
    rms = np.sum(audio_data * audio_data) ** 0.5
    return rms

def record_audio():
    # PyAudio configuration
    CHUNK = 1024 # Number of audio frames per buffer
    FORMAT = pyaudio.paInt16 # Audio format
    CHANNELS = 1 # Number of audio channels
    RATE = 44100 # Audio sample rate in Hz
    RECORD_SECONDS = 15 # Maximum recording time in seconds
    SILENCE_LENGTH = 1 # Minimum silence length to stop recording in seconds
    SILENCE_THRESHOLD = 0.001 # RMS threshold for detecting speech

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    print("Recording started...")

    # Record audio data until user stops speaking
    frames = []
    ring_buffer = np.zeros(RATE * SILENCE_LENGTH)
    silence_counter = 0
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        frames.append(data)

        # Add audio data to ring buffer
        ring_buffer = np.concatenate((ring_buffer[CHUNK:], audio_data))

        # Calculate RMS value of ring buffer
        rms = calculate_rms(ring_buffer)

        # Check if RMS value is below threshold
        if rms < SILENCE_THRESHOLD:
            silence_counter += 1
        else:
            silence_counter = 0

        # Stop recording if there is silence for more than SILENCE_LENGTH seconds
        if silence_counter > SILENCE_LENGTH:
            break

        # Stop recording if maximum recording time is reached
        if len(frames) >= RECORD_SECONDS*RATE/CHUNK:
            break

    print("Recording stopped...")

    # Close audio stream and PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to file
    wf = wave.open("output.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    print("Audio saved to file 'output.wav'")

# record_audio()
