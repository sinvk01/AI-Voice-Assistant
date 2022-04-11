import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing the background noises..Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("Ask me anything..")
        recorderaudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recorderaudio,language='english')
        print("Message",format(command))
    except Exception as ex:
        print(ex)

    if 'chrome' in command:
        a = 'Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        program =r"C:\Users\sinha\AppData\Local\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'play' in command:
        b = 'Opening youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)

