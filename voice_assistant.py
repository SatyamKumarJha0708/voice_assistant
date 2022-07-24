import pyttsx3 
import speech_recognition as sr
import datetime
import winshell
import wikipedia 
import webbrowser
import os
import smtplib
from email.message import EmailMessage
import pyjokes
import pywhatkit

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

def takeCommand(ask = False):
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        query = ''

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


dict = {'satyam':'satyamkj24764@gmail.com',
    'jha':'kumar.satyam0708@gmail.com'}

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('satyamkj24764@gmail.com', 'yfybsfubeoinqpal')
    email = EmailMessage()
    email['From'] = 'satyamkj24764@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def respond(query):
    
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        

        if  ' wikipedia'  in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'video' in query:
            speak('searching for video')
            pywhatkit.playonyt(query)

        elif 'google' in query:
            speak("What do you want to search for?")
            search = takeCommand("What do you want to search for?")
            url = 'http://www.google.com/search?q=' + search
            webbrowser.get().open(url)
            print('Here is what i found for' + search)

        elif 'location' in query:
            speak("What is the location?")
            location = takeCommand("What is the location?")
            url = 'http://www.google.nl/maps/place/' + location + '/&amp'
            webbrowser.get().open(url)
            print('Here is the location' + location)

        elif 'play music' in query:
            speak("Enjoy with some music")
            music_dir = 'D:\\my_music'
            songs = os.listdir(music_dir)
            print(songs) 
            # for i in range(0,2):  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif " the time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Time)    
            speak(Time)

        elif "clear my bin" in query:
            speak('Clearing trash')
            winshell.recycle_bin().empty(
                confirm = True, show_progress = False, sound = True
            )
        
        elif "joke" in query:
            joke_1=pyjokes.get_joke(language="en",category="all")
            print(joke_1)
            speak(joke_1)
        
        elif 'email to' in query:
            try:
                name = list(query.split()) 
                name = name[name.index('to')+1]
                speak("tell me the subject?")
                subject=takeCommand()
                speak("Tell me the text you wanna send?")
                content = takeCommand()
                to = dict[name]
                send_email(to,subject,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to send the email at the moment.Try again")
                
        elif "exit" in query:
            speak("I'm going to sleep now , Wake me up if you want something")
            exit()
wishMe()
query=takeCommand()
respond(query)
