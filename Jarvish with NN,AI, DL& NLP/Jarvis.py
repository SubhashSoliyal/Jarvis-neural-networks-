import random
import json
import torch
from Brian import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

device= torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


# ................................

Name = "jarvis"
from Listen import Listen
from Speak import Say
from Task import NonInputExecution, InputExecution

def Main():
    sentence = Listen()
    # result = str(sentence)

    
    sentence = tokenize(sentence)
    x = bag_of_words(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _ , predicted = torch.max(output,dim= 1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim= 1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.80:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if tag == "bye":
                    Say(reply)
                    exit()

                if tag == "time":
                    NonInputExecution(reply)

                elif tag == "date" :
                    NonInputExecution(reply)

                elif tag == "day" :
                    NonInputExecution(reply)

                elif tag == "wikipedia" :
                    result = str(sentence)
                    InputExecution(reply,result)
                    

                elif  tag == "google" :
                    result = str(sentence)
                    InputExecution(reply,result)
                    

                elif tag == "ChatGPT_Human_AI":
                    result = str(sentence) 
                    InputExecution(reply,result)
                    




                elif tag == "greeting":
                    
                    Say(reply)
                
                elif tag == "health":
                    Say(reply)

                elif tag == "identity":
                    Say(reply)
                
                elif tag == "namesta":
                    Say(reply)
                
                

                else:
                    Say(reply)

                tag = ""


# while True:
#     # if Listen() == "jarvis":
#     Main()



