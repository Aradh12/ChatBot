import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pandas as pd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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

    speak("I am your medibot I am here to help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def diagnosis():
    df=pd.read_csv('medibot\Training.csv')
    for i in df.columns[:-1]:
        if 1 in list(df[i]):
            print("do you feel",*i.split("_"))
            o=input()
            o.lower()
            if o=='yes':
                df= df[df[i] != 0]
    out=list(set(df['prognosis']))
    if len(out)==1:
        return ''.join(out)
    else:
        return ' and '.join(out)

if __name__ == "__main__":
    wishMe()
    
    speak('Please provide me some details before we start')
    
    speak('Please Enter your name')
    name=input('Name : ')
    
    speak('Please Enter your age')
    age=input('Age : ')
    
    speak('Please Enter your gender')
    gen=input('gender M/F/TG : ')

    print("Let's start the procedure of checking your disease ?\n")
    speak("Let's start the procedure of checking your disease")
    
    while True:
        dis=diagnosis()
        out=name,' you are suffering with',dis
        speak(out)
        print(out)

        print('Do you need the Doctor related to your disease ?')
        speak('Do you need the Doctor related to your disease')
        

        print('To retest give commomnd retest ')
        print('To shut down me say thank you')
        speak('To retest give commomnd retest or To shut down me say thank you')
        query=input().lower()
        #query = takeCommand().lower()

        if 'thank you' in query:
            speak('Have a good day to you')
            quit()