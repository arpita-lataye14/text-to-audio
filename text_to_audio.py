from cgitb import text
from email.mime import audio
from gtts import gTTS

from playsound import playsound

audio='speech.mp3'
language='en'
sp=gTTS(text='hello programmer, how are you',
        lang=language,slow=False)

sp.save(audio)
playsound(audio)