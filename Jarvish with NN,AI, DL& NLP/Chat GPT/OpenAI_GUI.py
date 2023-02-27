import tkinter as tk
import openai
import speech_recognition as sr
import pyttsx3
import os


openai.api_key = os.environ.get("OPENAI_API_KEY")

def listen_and_respond():
    # listen to the user's voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        # use Google Cloud Speech-to-Text API to convert audio to text
        user_input = r.recognize_google_cloud(audio, credentials_json=openai.api_key)
        print("You said: " + user_input)
        
        # use OpenAI to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        
        print("Chatbot: " + response)
        
        # use pyttsx3 to speak the response
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

root = tk.Tk()
root.title("Chatbot")

# create a button to start listening
listen_button = tk.Button(root, text="Listen", command=listen_and_respond)
listen_button.pack()

root.mainloop()
