import pyttsx3
import datetime

frase = str(input('Escribir una frase aqui '))

engine  = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak(frase)  