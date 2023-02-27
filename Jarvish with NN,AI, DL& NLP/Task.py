import datetime
from Speak import Say
from pyChatGPT import ChatGPT
import openai
import os


#  Function

#  Types

#1 - non Input
# eg: time, date, speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()

    elif "day" in query:
        Day()



# 2 - Input
# eg: google search, wikipedia
    

def InputExecution(tag,query):
    query =str(query).replace("jarvis","")

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("tall me abou","").replace("abou","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name,2)
        Say(result)
        tag = ".def"
        return tag

    elif "google" in tag:
        query = str(query).replace("google","").replace("search","")
        import pywhatkit
        pywhatkit.search(query)
        # tag = "."
        return tag

    elif "ChatGPT_Human_AI" in tag:
         # Set the API key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # openai .api_key = "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" #"YOUR_API_KEY"

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
        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "

        # ask =Listen()
        # ask = input(restart_sequence)
        

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=  restart_sequence + query + start_sequence,
        #"The following is a conversation with an AI assistant.
        # The assistant is helpful, creative, clever, and very friendly.
        # \n\nHuman: Hello, who are you?
        # \nAI: I am an AI created by OpenAI. How can I help you today?
        # \nHuman:  What do you need help with?",
        temperature=0.9,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

        # Print the generated text
        # message = completion.choices[0].text
        message = response['choices'][0]['text']
        Say(message)
        return message
        # print(message)