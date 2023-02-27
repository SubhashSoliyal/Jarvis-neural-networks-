import openai
import speech_recognition as sr 
import pyttsx3
import os
from googletrans import Translator
import tkinter as tk

root = tk.Tk()
# root.geometry("700x1000+0+0")
root.title("ChatGPT")

frame = tk.Frame(root)

scrollbar = tk.Scrollbar(frame)
chat_history = tk.Text(frame, height=150, width=500, yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
chat_history.pack(side='left', fill='both', expand=True)
# chat_history.config(state='disabled')
frame.pack()


file = open("open_AI_talk.txt","a")


def translate_to_hindi(text):
    translator = Translator(dest="hi")
    translated = translator.translate(text).text
    return translated

# input_text = input("Enter text to translate: ")
# translated_text = translate_to_hindi(input_text)
# print("Translated Text: ", translated_text)


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #4
    engine.setProperty('rate', 200)

    
    print("    ")
    print(f"A.I : {Text}")
    file.write(f"A.I : {Text}\n\n\n")
    # print(Text)
    engine.say(text= Text)
    engine.runAndWait()
    print("    ")


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
        print(f"You Said : {query}")
        file.write(f"YOu Said: {query}\n")
        # Say(f"You Said : {query}")


        # query1 = r.recognize_google(audio_data=audio,language='hi') # use this if not working
        # print(f"You Said : {query1}")
        # file.write(f"YOu Said: {query1}\n")
        # # Say(f"You Said : {query}")


    except:
        return "su"
        # query = str(query)
        # query1 = str(query1)
    return query


def openAI(query):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    start_sequence = "\nAI:"
    restart_sequence = "\n\nHuman: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= restart_sequence + query + start_sequence,
    # "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \nAI: I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific?\nHuman: \nAI: I'm happy to help in any way I can! What would you like assistance with?\nHuman: hello\nAI: Hi there! How can I help you today?\nHuman: wether\nAI: Are you looking for weather information? What city or region would you like to get a forecast for?\nHuman: good Are you looking for something good? I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific? Is there a task I can help you with? Please let me know if there is anything I can do for you.",
    temperature=0.9,
    max_tokens=1050,
    top_p=1,
    best_of=3,
    frequency_penalty=0.1,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    ) 
    message = response["choices"][0]["text"]
    
    chat_history.config(state='normal')
    chat_history.insert('end', 'You: ' + query + '\n')
    chat_history.insert('end', 'ChatGPT: ' + message + '\n\n')
    chat_history.config(state='disabled')
    # input_field.delete(0, 'end')
  
    
    return message





while True:
    query = Listen()

    if 'goodbye' in query or 'bye' in query or 'Goodbye' in query:
        # Say("Ok sir, bye! you can call me any time")
        Say(openAI(query= query))
        exit()  
    
    elif query == "su":
        Listen()
    
    elif 'open file' in query:
        with open("open_AI_talk.txt","r") as file:
            print(file.read())
    
    elif 'close file' in query:
        file.close()

    else: 
        # print(query)
        Say(openAI(query= query))
        
