import os
import openai
from Listening_Say_Function import Say, Listen

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:


    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    ask =Listen()
    # ask = input(restart_sequence)
    

    response = openai.Completion.create(
    model="text-davinci-003",
     prompt=  ask,#"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:  What do you need help with?",
    temperature=0.9,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    text = response['choices'][0]['text']
    # print( text)
    Say(text)