from elevenlabs import set_api_key
from elevenlabs import generate, play

set_api_key('0aa68134bd60c5b48690b07536907e6f')

def speak(text):
    text=str(text)
    audio=generate(
        text=text,
        voice="Daniel",
        model="eleven_multilingual_v2"
        )
    play(audio)
