import openai
import speech_recognition as sr
import pyttsx3 #pip install pyttsx3
import os




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

def OpenAI(query):
    
    # Set the API key
    openai.api_key = os.getenv("OPENAI_API_KEY") #"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" #"YOUR_API_KEY"

    # Use the `Completion` endpoint to generate text
    # model_engine = "text-davinci-002"
    # prompt = query

    # completion = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=  1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )


    # import os
    # import openai

    # openai.api_key = os.getenv("OPENAI_API_KEY")

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

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
    # Print the generated text
    # message = completion.choices[0].text
    message = response["choices"][0]["text"]
    return message
    # print(message)

while True:
      
    query = Listen()
    # print(query)
    # query = "Hello"
    # if 'jarvis' in query or 'hello' in query or 'bts lover' in query:
        # query = Listen()

    if 'goodbye' in query or 'bye' in query or 'Goodbye' in query:
        # Say("Ok sir, bye! you can call me any time")
        Say(OpenAI(query= query))
        exit()  
    
    elif query == "su":
        Listen()
    
    else: 
        # print(query)
        Say(OpenAI(query= query))





# ///
#         return data.encode('utf-8')
#     elif msg_in=='yes please':
#         data="show you the list of the product"
#         return data.encode('utf-8')
#     elif msg_in=='i am fat and sick':
#         data="diet chart"
#         return data.encode('utf-8')
#     else:
#         return msg_in.encode('utf-8')
# def open_connection(host='127.0.0.1',port=8888):

#     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     print('socket created')

#     try:
#         s.bind((host,port))
#     except socket.error as err:
#         print('bind failed.'+str(err[0]) + 'Message'+str(err[1]))
#         return


#     s.listen(10)

#     while True:

#         # wait to accept a connection - blocking call
#         conn, addr = s.accept()
#         print('Connected with ' + addr[0] + ':' + str(addr[1]))
#         path=r"C:\Users\MI\Desktop\Chatbot project\Chatbot\volley.png"

#         with open("volley.png", "rb") as f:
#             # Read the entire file as a single string
#             file_tol=f.read()
#             ftype="file"
#             msg_to_sender=icon_msg(file_tol,ptype=ftype)

#             for i in range(1):
#                 send_msg_(conn,msg_to_sender,ptype=ftype)

#             # msg=''
#             # msg=str(input('You>'))
#             send_msg(conn,'Testing...')

#         # msg = conn.recv(16384)

#         # print('Server received ', repr(msg))

#         # msg_to_sender=input('Server>')
#         # for i in range(0):
#         #     send_msg_(conn,msg_to_sender)

#             # msg=''
#             # msg=str(input('You>'))
#             #send_msg(conn,'Testing...')

#         # msg=''
#         # msg=str(input('You>'))
#         msg = conn.recv(16384)

#         print('Server received ', repr(msg))
#         msg_to_sender = input('Server>')
#         for i in range(0):
#             send_msg_(conn,msg_to_sender)


#             send_msg(conn,'Testing...')



#         '''
#         data=''
#         while True:
#             #msg_in=''
#             msg_in=str(input('You>'))
#             if msg_in!='exit' and msg_in!='':
#                 data=llllllllllllllllllllllllllllllllllllllllllllllllll(msg_in)
#                 send_msg_(conn,data,ptype=ftype)


#             else:
#                 send_msg_(conn,'System exit...')
#                 #msg=str(input('You>'))
#                 data=llllllllllllllllllllllllllllllllllllllllllllllllll(msg_in)
#                 send_msg_(conn,data,ptype=ftype)
#                 break

#             msg = conn.recv(16384)

#             if msg!=b'':
#                 print('Server>', repr(msg))
#                 msg_to_sender=input('Server>')
#                 for i in range(0):
#                     send_msg_(conn,msg_to_sender)
#         '''
# open_connection()
# ///