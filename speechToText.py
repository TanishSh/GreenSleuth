import whisper

model = whisper.load_model("small.en")

def speechToText(audioFile):
    result = model.transcribe(audioFile)
    return result["text"]


# str = speechToText("test3.wav")
# print(str)