import os
import openai
from Listening_Say_Function import Say, Listen

talk = True
def OpenAI_you(you):

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= you,
    # Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
    temperature=0.5,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.7,
    presence_penalty=0.0,
    best_of = 3,
    stop=["You:"]
    )
    return response['choices'][0]['text']


# def OpenAI_Friend(Friend):
    
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=Friend,
#     # You: Did you watch anything interesting?\nFriend:",
#     temperature=0.5,
#     max_tokens=60,
#     top_p=1.0,
#     frequency_penalty=0.5,
#     presence_penalty=0.5,
#     stop=["Friend:"]
#     )
#     return response['choices'][0]['text']


You = input("Enter your quesion? :- ")
# Friend = ""
temp = True
while talk:
   
    if temp == True:
        ask =  You
        # print(You)
        Friend = OpenAI_you(ask)
        Say(Friend)
        temp = False
        

    elif  temp == False:
        ask = Friend
        You = OpenAI_you(ask)
        # print (You)
        Say(You)
        temp = True
        # talk = False
        
        
    # print(OpenAI_you("hello",n))
    