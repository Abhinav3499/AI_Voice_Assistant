import speech_recognition as sr

def transcribe_audio_google(file_path="output.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        print("Transcribing with Google API...")
        text = recognizer.recognize_google(audio)
        print(f"Transcript: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"🔌 API error: {e}")
        return None

if __name__ == "__main__":
    transcribe_audio_google("output.wav")
