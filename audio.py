import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="output.wav", duration=5, sample_rate=44100):
    os.makedirs("recordings", exist_ok=True)
    filepath = f"recordings/{filename}"
    print("Recording for 5 seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait() 
    write(filepath, sample_rate, audio)
    print(f"Recording saved as '{filepath}'")
    return filepath

if __name__ == "__main__":
    record_audio()
