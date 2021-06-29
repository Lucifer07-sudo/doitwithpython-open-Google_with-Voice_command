





import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from urllib.request import urlopen
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 #print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Penny Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #try other languages
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) 
        print("Say that again please")   
        speak("Say that again please")  #try speak instead of print
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

 
      
                 
        if 'open google' in query:
            speak ('opening google')
            from selenium import webdriver
            chromedriver="C:\Webdriver\chromedriver"
            driver =webdriver.Chrome(chromedriver)
            driver.get("https://google.com")
            

        elif 'close google' in query or 'kill google' in query:
            speak('closing google')
            from selenium import webdriver
            chromedriver="C:\Webdriver\chromedriver"
            driver.quit()
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')           
            sys.exit()
                                            


