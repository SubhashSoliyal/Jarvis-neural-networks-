import openai
import gradio as gr
import os
import speech_recognition as sr 
import pyttsx3



query = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \nAI: I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific?\nHuman: \nAI: I'm happy to help in any way I can! What would you like assistance with?\nHuman: hello\nAI: Hi there! How can I help you today?\nHuman: wether\nAI: Are you looking for weather information? What city or region would you like to get a forecast for?\nHuman: good Are you looking for something good? I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific? Is there a task I can help you with? Please let me know if there is anything I can do for you.",

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id) #4
    engine.setProperty('rate', 175)

    print("    ")
    print(f"A.I : {Text}")
    # print(Text)
    engine.say(text= Text)
    engine.runAndWait()
    print("    ")
# Say("Hello bro")

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
        # Say(f"You Said : {query}")


    except:
        return "su"
        # query = str(query)
        # query1 = str(query1)
    return query


def openai_create(query):
    
    # Set the API key
    openai.api_key = os.getenv("OPENAI_API_KEY") 

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= restart_sequence + query + start_sequence,
    
    temperature=0.9,
    max_tokens=1050,
    top_p=1,
    best_of=3,
    frequency_penalty=0.1,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    ) 
    # Print the generated text
    # message = completion.choices[0].text
    message = response["choices"][0]["text"]
    return message

def Chatgpt_clone(input,history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)

    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history,history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Build your own ChatGPT with OpenAI & Gradio </center></h1>""")

    listion = gr.Audio(Say(query))
    chatbot = gr.Chatbot()
    massage = gr.Textbox(placeholder = query)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(Chatgpt_clone, inputs= [massage , state], outputs = [chatbot, state])

block.launch(debug = True)
