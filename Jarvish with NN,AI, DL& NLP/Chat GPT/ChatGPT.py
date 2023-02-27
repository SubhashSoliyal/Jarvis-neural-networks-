import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def Friend_Chat(ask):
    ask =ask
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= ask, #"You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:"+ ask,
    temperature=0.5,
    max_tokens=600,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )

    return response["choices"][0]["text"]

while True:

    ask= input("you: ")
    print("Friend:" + Friend_Chat(ask))
    