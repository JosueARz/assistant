import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia 
import webbrowser
import pywhatkit
import os 
import pyautogui
import psutil
import pyjokes

engine  = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id )
newVoiceRate = 150  ## velocidad en la que hablará, x palabras por minuto
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

def sch():
    speak('what should i search?')
    try:
        pywhatkit.search(takeCommand().lower())
        speak('i found that') 
    except:
        speak('An unknown error occured')
def yt():
    speak('what should i play')
    try:
         pywhatkit.playonyt(takeCommand().lower())
         speak('i found that')
    except:
        speak("Network Error Occured")

def inf():
    speak('What do you need information about?')
    try:
        pywhatkit.info(takeCommand().lower(), lines = 4)
        speak('i found that')
    except:
        speak("An Unknown Error Occured")
         

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com', '123test')
    server.sendmail('test@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\gmgar\\Documents\\Data_science\\DT_SC\\github\\asistente de voz\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    speak('CPU is at' )
    speak(usage)
    speak('Nivel of the battery is ')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())
    

if __name__ == "__main__":
    print(' What i can do and its commands')
    print('1- hour: time')
    print('2- date: date')
    print('3- search on wikipedia: wikipedia -- tell you want to search on wikipedia --')
    print('4- open a website: search on internet ')
    print('5- search something in google: search web-- tell something you want search--')
    print('6- play something in youtube: play youtube -- tell you want to play--')
    print('7- resume aoubt somthing: info -- tell that thing you want a resume--')
    print('8- close pc session: logout')
    print('9- shutdown pc: shutdown ')
    print('10- restart pc: restart')
    print('11- save a reminder: remember')
    print('12- listen the reminder: tell me my reminders')
    print('13- take a screenshot: screenshot')
    print('14- cpu and battery nivels: pc info')
    print('15- listen a joke: tell me a joke')
    print('16- end assitant: bye')
    welc()
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        
        elif 'date' in query:
            date()
       
        elif 'bye' in query:
            quit() 
               
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 1)
            speak(result)
        
        elif 'sendmail' in query:
            try:
                speak('what hould i say?')
                content =  takeCommand().lower()
                to = 'guitjar@gmail.com'
                #sendmail(to, content)
                speak('e_mail sent')
            except Exception as  e:
                speak(e)
                speak('fail to sent')
        
        elif 'search on internet' in query:
            speak('What should i search?')
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            search = (takeCommand().lower() + '.com')
            print(search)
            webbrowser.get('chrome').open_new_tab(search)
            
        elif 'search web' in query:
            sch()
        
        elif 'play youtube' in query:
            yt()
        
        elif 'info' in query:
            inf()
        
        elif 'logout' in query:
            os.system('shutdown - l ')
            
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
            
        elif 'restart' in query:
            os.system('shutdown /r /t 1')    
            
        elif 'remember' in query:
            speak('What should i remember')
            data = takeCommand().lower()
            speak('You say me to remember: ' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        
        elif 'tell me my reminders' in query:
            remember = open('data.txt', 'r')
            speak('you say me to remember')
            speak(remember.read())
            
        elif 'screenshot' in query:
            screenshot()
            speak('Done!')
      
        elif 'pc info' in query:
            cpu()
         
        elif 'tell me a joke'  in query:
            jokes()
           