import asyncio
from audio import record_audio
from STT import transcribe_audio_google
from query import generate_response
from TTS import text_to_speech

def main():
    print("=== Step 1: Recording Audio ===")
    audio_file = record_audio()  
    
    print("\n=== Step 2: Speech-to-Text (STT) ===")
    transcript = transcribe_audio_google(audio_file)
    if transcript is None:
        print("Transcription failed. Exiting.")
        return
    
    print("\n=== Step 3: Query Gemini ===")
    gemini_response = generate_response(transcript)
    if gemini_response is None:
        print("Query failed. Exiting.")
        return
    
    print("\n=== Step 4: Text-to-Speech (TTS) ===")
    asyncio.run(text_to_speech(gemini_response))

if __name__ == "__main__":
    main()
