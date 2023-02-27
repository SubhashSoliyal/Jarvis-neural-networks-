import tkinter as tk
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def listen_and_respond():
    # listen to the user's voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        # convert the audio to text
        user_input = r.recognize_google(audio)
        print("You said: " + user_input)
        
        # process the user's input and generate a response
        response = "This is a sample response from the chatbot."
        print("Chatbot: " + response)
        
        # convert the response to speech
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
