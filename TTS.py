import asyncio
from edge_tts import Communicate

async def text_to_speech(text: str, voice: str = "en-IN-PrabhatNeural"):
    communicate = Communicate(text=text, voice=voice)
    await communicate.save("output.mp3")
    print("Audio saved as output.mp3")

if __name__ == "__main__":
    sample_text = "My name is Abhinav Arya"
    asyncio.run(text_to_speech(sample_text))
