import asyncio
import os
from edge_tts import Communicate

async def text_to_speech(text: str, voice: str = "en-IN-PrabhatNeural"):
    output_path = os.path.join("static", "output.mp3")
    communicate = Communicate(text=text, voice=voice)
    await communicate.save(output_path)
    print(f"Audio saved as {output_path}")

if __name__ == "__main__":
    sample_text = "My name is Abhinav Arya"
    asyncio.run(text_to_speech(sample_text))
