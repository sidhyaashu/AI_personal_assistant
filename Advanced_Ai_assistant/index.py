#IMPORTS
import pyttsx3 #to convert speech to text
import speech_recognition as sr #to recognize speech
import webbrowser #to serve website
import pywhatkit #to search in google
from bs4 import BeautifulSoup
import wikipedia
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from tkinter import StringVar
import datetime
from pywikihow import search_wikihow
from googletrans import Translator
from gtts import gTTS
import PyPDF2
from pytube import YouTube
from playsound import playsound
import keyboard
import pyjokes



# function for Listening and recognize
def listeningAndrecognige():
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print("Listening....")
            recognizer.adjust_for_ambient_noise(source) #to avoid extra noice from microphone
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source) #to listen the source
            try:
                print("Recognizing....")
                data = recognizer.recognize_google(audio)
                return data.lower()
                break
            except sr.UnknownValueError:
                repeate = "Please say again...!!"
                Speech(repeate)
            
# function for speeck
def Speech(x):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') #to get system voice
    engine.setProperty('voice',voices[0].id) #to set System voice
    rate = engine.getProperty('rate') #to controle voice speed rate
    engine.setProperty('rate',150)
    engine.say(x) #to start speech
    engine.runAndWait()
    

if __name__ == '__main__': #to split the code 
    
  
    if "rama" in listeningAndrecognige().lower():
        Speech("Hii sir How may i help you")
        
    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()

        if 'akeli' in musicName:
            os.startfile('E:\\Songs\\akeli.mp3')

        elif 'blanko' in musicName:
            os.startfile('E:\\Songs\\blanko.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")

    def Temp():
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("no problem sir")

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'india' in name:

            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'europe' in name:
            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak(Text)
        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def screenshot():
        while True:
            command = listeningAndrecognige().lower() 
            if "how are you" in command:
                Speech("I am find Sir")
            elif "search in youtube" in command:
                Speech("Ok sir that what i found in youtube")
                command = command.replace("search in youtybe","")
                web = "https://www.youtube.com/results?search_query="+command
                webbrowser.open(web)
                Speech("Done sir")
            elif "search in google":
                Speech("Ok sir that what i found in google")
                command = command.replace("search in google","")
                pywhatkit.search(command)
                Speech("Done sir")
            elif "website":
                Speech("Ok sir launching")
                command = command.replace("website","")
                web1 = command.replace("open","")
                web2 = 'https://www.'+web1+'.com'
                webbrowser.open(web2)
                Speech("Done sir")
            
            elif 'launch' in query:
                Speak("Tell Me The Name Of The Website!")
                name = takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'wikipedia' in query:
                Speak("Searching Wikipedia.....")
                query = query.replace("jarvis","")
                query = query.replace("wikipedia","")
                wiki = wikipedia.summary(query,2)
                Speak(f"According To Wikipedia : {wiki}")

            elif 'screenshot' in query:
                screenshot()

            elif 'open facebook' in query:
                OpenApps()

            elif 'open instagram' in query:
                OpenApps()

            elif 'open maps' in query:
                OpenApps()

            elif 'open code' in query:
                OpenApps()

            elif 'open youtube' in query:
                OpenApps()
                
            elif 'open telegram' in query:
                OpenApps()

            elif 'open chrome' in query:
                OpenApps()

            elif 'close chrome' in query:
                CloseAPPS()

            elif 'music' in query:
                Music()

            elif 'close telegram' in query:
                CloseAPPS()

            elif 'close instagram' in query:
                CloseAPPS()

            elif 'close facebook' in query:
                CloseAPPS()

            elif 'pause' in query:
                keyboard.press('space bar')

            elif 'restart' in query:
                keyboard.press('0')

            elif 'mute' in query:
                keyboard.press('m')

            elif 'skip' in query:
                keyboard.press('l')

            elif 'back' in query:
                keyboard.press('j')

            elif 'full screen' in query:
                keyboard.press('f')

            elif 'film mode' in query:
                keyboard.press('t')

            elif 'youtube tool' in query:
                YoutubeAuto()

            elif 'close the tab' in query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in query:
                keyboard.press_and_release('ctrl +h')

            elif 'chrome automation' in query:
                ChromeAuto()

            elif 'joke' in query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my word' in query:
                Speak("Speak Sir!")
                jj = takecommand()
                Speak(f"You Said : {jj}")

            elif 'my location' in query:
                Speak("Ok Sir , Wait A Second!")
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'alarm' in query:
                Speak("Enter The Time !")
                time = input(": Enter The Time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time To Wake Up Sir!")
                        playsound('iron.mp3')
                        Speak("Alarm Closed!")

                    elif now>time:
                        break

            elif 'video downloader' in query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                Speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                Speak("Video Downloaded")
                
            elif 'translator' in query:
                Tran()
            
            elif 'remember that' in query:
                remeberMsg = query.replace("remember that","")
                remeberMsg = remeberMsg.replace("jarvis","")
                Speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in query:
                remeber = open('data.txt','r')
                Speak("You Tell Me That" + remeber.read())

            elif 'google search' in query:
                import wikipedia as googleScrap
                query = query.replace("jarvis","")
                query = query.replace("google search","")
                query = query.replace("google","")
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(query)

                try:
                    result = googleScrap.summary(query,2)
                    Speak(result)

                except:
                    Speak("No Speakable Data Available!")

            elif 'how to' in query:
                Speak("Getting Data From The Internet !")
                op = query.replace("jarvis","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                Speak(how_to_func[0].summary)
                
            elif 'temperature' in query:
                Temp()

            elif 'read book' in query:
                Reader()
    else:
        print("Thank You")