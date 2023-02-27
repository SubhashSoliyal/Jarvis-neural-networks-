import openai
import speech_recognition as sr 
import pyttsx3
import os
from googletrans import Translator

file = open("OutPut_FIle_OpenAI.txt","a")
quesion = open("Quesion_FIle.txt","r",errors="ignore")
# q_lenth = len(quesion.readlines())
# quesion.close()

def translate_to_hindi(text):
    translator = Translator(dest="hi")
    translated = translator.translate(text).text
    return translated


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #4
    engine.setProperty('rate', 200)

    
    print("    ")
    print(f"A.I : {Text}")
    # file.write(f"AI: {Text}\n\n\n")
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
        query = r.recognize_google(audio_data=audio,language='en-in') # use this if not working
        print(f"You Said : {query}")
        file.write(f"YOu Said: {query}\n")
        # Say(f"You Said : {query}")

    except:
        return "su" 
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
    max_tokens=750,
    top_p=1,
    best_of=3,
    frequency_penalty=0.1,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    ) 
    message = response["choices"][0]["text"]
    
    return message

  
for x in quesion:
    # print(x)
    result= openAI(x)
    file.write(f"You Said: {x}\n")
    Say(x)
    file.write(f"AI: {result}\n\n\n")
    Say(result)
    

        
    






# while True:
#     query = Listen()

#     if 'goodbye' in query or 'bye' in query or 'Goodbye' in query:
#         # Say("Ok sir, bye! you can call me any time")
#         Say(openAI(query= query))
#         exit()  
    
#     elif query == "su":
#         Listen()
    
#     elif 'open file' in query:
#         with open("open_AI_talk.txt","r") as file:
#             print(file.read())
    
#     elif 'close file' in query:
#         file.close()

#     else: 
#         # print(query)
#         Say(openAI(query= query))
        
