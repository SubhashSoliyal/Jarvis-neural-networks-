import speech_recognition as sr
import pyttsx3 #pip install pyttsx3

import os


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    
    engine.setProperty('voices',voices[4].id) #for hindi use id 4,
    # print(voices[4].id)
    engine.setProperty('rate', 175)

    # print("    ")
    # print(f"A.I : {Text}")
    print(Text)
    engine.say(text= Text)
    engine.runAndWait()
    # print("    ")
# Say("Hello bro kese ho tum")

def Listen():
    
    r = sr.Recognizer()
    

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source) # you can use 0,4 also init

    try:
        print("Recognizing....")
        # query = r.recognize_amazon(audio,bucket_name= 'en-in')
        
        query = r.recognize_google(audio_data=audio,language='en-in') # use this if not working
        # query1 = r.recognize_google(audio_data=audio,language='hi') # use this if not working
        print(f"You Said : {query}")
        # print(f"You Said : {query1}")


    except:
        return "su"
        # query = str(query)
        # query1 = str(query1)
    return query