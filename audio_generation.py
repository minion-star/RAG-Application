from elevenlabs import play, stream, save
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()

def save_audio(text):

    client = ElevenLabs(
        api_key= os.getenv('ELEVENLABS_API_KEY'),
    )

    audio = client.generate(
        text = text,
        voice = "Rachel",
        model = "eleven_multilingual_v2"
    )

    save(audio, "article.mp3")