import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import email.utils
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',150)


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
        speak("Good Evening")  

    speak(" hello sir, i'm your voice asssistant. how can i help you? ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("I'm Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Please say that again sir ...") 
        speak("Please say that again sir ...") 
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        

        if  'search for'  in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\my_music'
            songs = os.listdir(music_dir)
            print(songs) 
            # for i in range(0,2):  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif " the time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Time)    
            speak(Time)

        elif 'open vs code' in query:
            vscodePath = "C:\\Users\\Satyam Jha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        
        elif 'open careerride' in query:
            webbrowser.open('careerride.com')

        elif 'open prep insta' in query:
            webbrowser.open('prepinsta.com')
        
        elif "joke" in query:
            joke_1=pyjokes.get_joke(language="en",category="all")
            print(joke_1)
            speak(joke_1)
                
        elif "exit" in query:
            speak("I'm going to sleep now , Wake me up if you want something")
            exit()
        
