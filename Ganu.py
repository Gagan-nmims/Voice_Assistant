import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from googlesearch import *
import wolframalpha
 
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Ganu. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.phrase_threshold = 1
        #r.dynamic_energy_adjustment_damping = 1
        #r.energy_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"You said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)   #for error printing 
        print("Sorry!! Please repeat..")
        speak("Sorry!! Please repeat..")   
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower() 
        
        #Converting user query into lower case
        if 'wikipedia' in query:
            speak('Searching Wikipedia...Please Wait')
            print("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\gagan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%Y/%m/%d")
            speak(f"the date is {strTime}")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=9mQJaXwGPlg&list=PLPFUHdSXZRCKrFQhqEVAaJpzQ2CBO8sWH&index=1")

        elif 'who is gagan' in query:
            speak("Gagan is the creator of this application, here is the way you can reach out to him")
            webbrowser.open("https://www.facebook.com/gagan4uhh")

        elif 'who are you' in query:
            speak("Hello!! I am Ganu ")
    
        elif 'hello' in query:
            speak("Hello there!")
        
        elif 'when are you created' in query:
            speak("I was developed on 25th november 2019")
        
        elif 'who is Chanchal' in query:
            speak("She is professor of CSJM")

        elif 'who is harvinder' in query:
            speak("Harvinder is sister of gagan")


        elif 'who is harleen' in query:
            speak("harleen is niece of gagan")

        
        elif 'why' in query:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")
        
        elif 'who' in query:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")

        elif 'what' in query:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")

        elif 'when' in query:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")

        elif 'where' in query:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")

        elif 'goodbye' in query:
            speak('Ok!, See you soon')
            quit()
            




