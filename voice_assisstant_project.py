import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import os
import random
import smtplib
from time import *

from tkinter import *
from tkinter.ttk import *

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():

    hour = int(datetime.datetime.now().hour)

    if hour < 12 and hour >= 0:
        speak("Good Morning....")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon....")
    elif hour > 16:
        speak("Good Evening....")
    speak("This is your voice assisstant, how may i help you ")


def search_web(input):
    speak('What do you want to search ?')
    search=audio_input()

    if 'youtube' in input.lower(): 
  
        speak('Searching in youtube')
        webbrowser.open("http://www.youtube.com/results?search_query=" + search)
        
    elif 'wikipedia' in input.lower(): 
  
        speak('Searching wikipedia')
        webbrowser.open("https://en.wikipedia.org/wiki/" + search) 
  
    else: 
  
        if 'google' in input: 
  
            speak('Searching google')
            webbrowser.open("https://www.google.com/search?q=" + search) 
  

def audio_input():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak('Listening....')
        print('Listening....')
        r.pause_threshold = 1
        input = r.listen(source)
    try:
        speak('Recognizing....')
        print("Recognizing....")
        audio = r.recognize_google(input, language='en-in')
        print(f'You said : {audio}')
        return audio
    except Exception as ex:
        print('Please try again !!')
        return None


def email_win():

    sen = ''
    rec = ''
    password = ''
    re = Tk()
    re.geometry('350x350')
    re.title('Email')
    l1 = Label(re, text="Enter you email address  : ")
    l2 = Label(re, text="Enter the receiver's address : ")
    l3 = Label(re, text="Enter password : ")
    e1 = Entry(re)
    e2 = Entry(re)
    e3 = Entry(re, show='*')
    
    def get_val():

        sen = str(e1.get())
        rec = str(e2.get())
        password = str(e3.get())
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sen, password)

            speak("What do you want to send ?")
            content = audio_input()
            print(content)
            speak('Do you want to send this e-mail : yes or no')
            if(audio_input() == 'yes'):
                s.sendmail(sen, rec, content)
                speak("Email sent....")
                s.quit()

            else:
                speak("Ok")
                speak('Do you want to exit ?')
                r=audio_input()
                if 'yes' in r:
                    re.destroy()
                else:
                    pass    

        except Exception as e:
            speak("Could not send email")

    b1 = Button(re, text='SUBMIT', command=get_val)
    b2=Button(re,text='CLOSE',command=re.destroy)
    b1.place(x=110, y=280)
    b2.place(x=200,y=280)
    l1.place(x=20, y=80)
    l2.place(x=20, y=140)
    l3.place(x=20, y=200)
    e1.place(x=180, y=80)
    e2.place(x=180, y=140)
    e3.place(x=180, y=200)        
    re.mainloop()

    # main function


def ai_main():
    global flag
    if flag:
       wish()
    flag=False
    try:

        audio = audio_input()
        audio = audio.lower()

        if 'wikipedia' in audio:
            
            audio = audio.replace('wikipedia', '')
            result = wiki.summary(audio, sentences=2)
            if result == None:
                speak('Nothing found')
            else:
                speak("According to Wikipedia....")
                speak(result)
        elif 'search' in audio:

            search_web(audio)

        elif 'who are you' in audio:

            speak('I am your voice assisstant !')

        elif 'play music' in audio:

            try:
                music_dir = 'C:\\Users\\anike\\OneDrive\\Documents\\Rockstar Games\\GTA V\\User Music'
                music_list = os.listdir(music_dir)
                os.startfile(os.path.join(
                    music_dir, music_list[random.randint(0, len(music_list))]))

            except Exception as e:
                speak("Sorry, unable to play music....")

        elif 'close' in audio or 'quit' in audio:

            speak('Shutting down')
            r.destroy()

        elif 'email' in audio:

            email_win()

        elif 'who made you' in audio:

            speak('I have been created by Aniket')
            
    except Exception as e:

        speak('I did not get what you said !')

flag=True
r = Tk()
r.title("Voice Assisstant")
r.geometry('300x300')
loadimage = PhotoImage(master=r, file="img1.png")
b11 = Button(r, width=25, image=loadimage, command=ai_main)
b12 = Button(r, text='QUIT', command=r.destroy)
b11.place(x=120, y=110)
b12.place(x=113, y=260)
r.mainloop()
