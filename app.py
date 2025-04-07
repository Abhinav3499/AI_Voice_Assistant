from flask import Flask, render_template, request, redirect, url_for
from audio import record_audio
from STT import transcribe_audio_google
from query import generate_response
from TTS import text_to_speech
import asyncio
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    response_text = ""
    if request.method == "POST":
        # Step 1: Record Audio
        audio_path = record_audio(duration=5)

        # Step 2: Transcribe
        transcript = transcribe_audio_google(audio_path)
        if not transcript:
            transcript = "Speech not recognized."
            return render_template("index.html", transcript=transcript, response=response_text)

        # Step 3: Generate Gemini response
        response_text = generate_response(transcript)
        if not response_text:
            response_text = "Error from Gemini API."
            return render_template("index.html", transcript=transcript, response=response_text)

        # Step 4: TTS
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        asyncio.run(text_to_speech(response_text))
    
    return render_template("index.html", transcript=transcript, response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
