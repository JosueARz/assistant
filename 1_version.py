import pyttsx3
import datetime
import speech_recognition as sr

engine  = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id )
newVoiceRate = 120  
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('Its')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    speak('The year is')
    speak(year)
    month = int(datetime.datetime.now().month)
    speak('The number of the month is')
    speak(month)
    day = int(datetime.datetime.now().day)
    speak('The day is')
    speak(day)

def  welc():
    speak('Welcome back sir!')
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak('Good morning')
    else:
        if hour >12 and hour <= 18:
            speak('Good aftrnoon')
        else:
            if hour > 18 and hour <= 24:
                speak('Good evening')
            else:
                speak('Good night')
        
    speak('How can i hel you')

welc()

def takeCommand():
    r = sr.Recognizer()
        
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("Listening... ")
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio, language = "es-ES")
        print(text)
    except:
        print("sorry, could not recognise")
        return "None"
    return text
takeCommand()