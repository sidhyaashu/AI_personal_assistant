import pyttsx3 # text to speech
import speech_recognition as sr #to recognition the speech
import webbrowser #to search webbrowser
import datetime #to show date and time
import pyjokes  #to make jokes
import time

#function for speech to text
def spText():
    recognizer = sr.Recognizer() 
    with sr.Microphone(device_index=0) as source: #to accese microphone
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source) #to reduce source noice
        audio = recognizer.listen(source) #to listen the source
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand ")
            
            
#function for Speech to text         
def speechToTxt(x):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') #to get system voice
    engine.setProperty('voice',voices[0].id) #to set System voice
    rate = engine.getProperty('rate') #to controle voice speed rate
    engine.setProperty('rate',150)
    engine.say(x) #to start speech
    engine.runAndWait()
    
    
    
    
if __name__ == '__main__': #to split the code 
    
    if "hey rama" in spText().lower():
        while True:
            data1 = spText().lower()
            if "your name" in data1:
                name = "my name is rama"
                speechToTxt(name)
            elif "old are you" in data1:
                age = "i am two years old"
                speechToTxt(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechToTxt(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                joke_1 =pyjokes.get_joke(language="en",category="neutral")
                speechToTxt(joke_1)
            elif "exit" in data1:
                speechToTxt("Thank you")
                break
            
            time.sleep(2)
    else:
        print("thanks")