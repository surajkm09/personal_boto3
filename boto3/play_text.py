from gtts import gTTS   # text to speech converting library
import os               #to execute commands on system
#from blink import blink

def play_text(s):
    tts = gTTS(text=s, lang='en') #text is converted into audio file here
    tts.save("audio.mp3")         # audio file is saved with name audio.mp3
    #blink()
    os.system("afplay audio.mp3")   #the audio file is played using afplay command
    return