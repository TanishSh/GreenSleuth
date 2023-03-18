import whisper

model = whisper.load_model("medium.en")

def speechToText(audioFile):
    result = model.transcribe(audioFile)
    return result["text"]


# str = speechToText("audio.mp3")
# print(str)
