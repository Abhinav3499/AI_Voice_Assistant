from flask import Flask, render_template, request, jsonify
from audio import record_audio
from STT import transcribe_audio_google
from query import generate_response
from TTS import text_to_speech
import asyncio
import time
import os

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_audio():
    audio_file = record_audio()  

    transcript = transcribe_audio_google(audio_file)
    if not transcript:
        return jsonify({"error": "Could not transcribe audio"}), 500

    response_text = generate_response(transcript)
    if not response_text:
        return jsonify({"error": "Gemini API failed"}), 500

    output_path = "static/output.mp3"
    if os.path.exists(output_path):
        os.remove(output_path)
    asyncio.run(text_to_speech(response_text))

    timestamp = int(time.time())  

    return jsonify({
        "response": response_text,
        "audio_url": f"/static/output.mp3?ts={timestamp}"
    })

if __name__ == "__main__":
    app.run(debug=True)
