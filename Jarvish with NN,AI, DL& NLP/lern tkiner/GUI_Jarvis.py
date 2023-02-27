import os

try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
    import pyttsx3

try: 
    import datetime
except:
    os.system('pip install datetime')
    import datetime

try:
    import speech_recognition as sr
except:
    os.system('pip install SpeechRecognition')
    import speech_recognition as sr

try: 
    import pyautogui
except:
    os.system('pip install pyautogui')
    import pyautogui

try:
    from time import sleep
except:
    os.system('pip install time')
    from time import sleep

try:
    import wikipedia
except:
    os.system('pip install wikipedia')
    import wikipedia

try:
    import win32api
except:
    os.system('pip install pywin32')
    import win32api

try:
    import webbrowser
except:
    os.system('pip install pycopy-webbrowser')

try:
    import winshell
except:
    os.system('pip install winshell')
    import winshell

try:
    import requests
except:
    os.system('pip install requests')
    import requests

# used in GUI after this
try:
    import random
except:
    os.system('pip install random')
    import random

try:
    import threading
except:
    os.system('pip install threading')
    import threading

try:
    import tkinter
    # from tkinter import *
except:
    os.system('pip install tk')
    import tkinter
    # from tkinter import *

try:
    import sys
except:
    os.system('pip install sys')
    import sys


# root = Tk()
# root.title('Jarvis Online')

# button = Button(root, text= 'Exit', width= 25, command= root.destroy)
# button.pack()

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 200)
    # print(voices[4].id) #hindi at 4
    engine.say(audio)
    engine.runAndWait()

speak('Initializing JARVIS......')

# url = "https://www.youtube.com/watch?v=T5lxctG5WMI"
# timeout = 5
# try:
#     request = requests.get(url, timeout= timeout)
#     print("Connectted to the Internet")
#     speak("INTERNET Connection detected")
#     speak("All systems have been Activated")
#     speak("you are online now!")
# except (requests.ConnectionError, requests.Timeout) as exception:
#     print("No Internet Connection")
#     speak("NO Internet connection Detected....")
#     speak("Shutting down the program.")
#     win32api.MessageBeep()
#     win32api.MessageBox(0, 'you are not connected to internet, Please make sure you connected to the Internet.')
#     speak("Thanks for giving me your time")
#     # exit()

# mainloop()

screen_main = tkinter.Tk()
screen_main.configure(background= 'black')
screen_main.attributes('-fullscreen',True)

def color_changer():
    color= ['red', 'gold','silver','cyan','magenta']
    actual_color= random.choice(color)
    lable.configure(foreground=actual_color )
    lable.after(1000, color_changer)

def font_changer():
    font_C= ['Arial', 'Arial Italic','	Arial Bold','Arial Bold Italic',
             'Bahnschrift *','Calibri Italic','Cambria','	Cambria Italic',
             'Cambria Bold','Candara Italic','	Comic Sans MS Italic','	Comic Sans MS'
             'Calibri Light','Calibri Light Italic','Calibri','SimSun']
    actual_font= random.choice(font_C)
    return actual_font
    # lable.configure(foreground=actual_font )
    # lable.after(1000, font_changer)

lable =tkinter.Label(screen_main, font= (font_changer,35),text= 'Created By Subhash',background= 'black')
color_changer()                 #Arial
lable.place(x= 1300, y= 45)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  


class Redirect():
    def __init__(self, widget, autoscroll= True):
        self.widget = widget
        self.autoscroll = autoscroll

    def Write(self, text):
        self.widget.insert('end','text')
        if self.autoscroll:
            self.widget.see('end') # autoscroll


def run():
    # use wishMe as a function which you want to run continuasly
    threading.Thread(target= wishMe).start()
    # threading.Thread(target= Main).start()

    def flush(self):
        pass

def guide_task():
    print("hey! There I am Jarvis")
    print("I can help you with variety of tasks")

def guide_run():
    threading.Thread(target= guide_task).start()
    

terminal = tkinter.Text(screen_main)
terminal.configure(background='black',foreground= 'white')
terminal.configure(width=60, height=30)
terminal.configure(font=('arial',10))
terminal.place(x=5,y=100)

guide_run()

old_stdout = sys.stdout
sys.stdout = Redirect(terminal)


initate_btn =tkinter.Button(screen_main, font=(font_changer,25),
                            foreground= 'cyan',background='black',
                            text="Initiate",command= wishMe)
# use wishMe as a function which you want to run continuasly
initate_btn.place(x= 1300, y=250)



screen_main.mainloop()



