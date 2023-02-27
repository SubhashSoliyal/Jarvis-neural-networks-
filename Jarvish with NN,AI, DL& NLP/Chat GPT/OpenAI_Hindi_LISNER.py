import openai
import speech_recognition as sr
import pyttsx3 #pip install pyttsx3


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voices',voices[8].id)
    # for i in range (0,6):
    #     print(voices[i].id)
    engine.setProperty('rate', 175)

    print("    ")
    print(f"A.I : {Text}")
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
        
        # query = r.recognize_google(audio_data=audio,language='en-in') # use this if not working
        query1 = r.recognize_google(audio_data=audio,language='hi') # use this if not working
        # print(f"You Said : {query}")
        print(f"You Said : {query1}")


    except:
        return "Need Change to google recognizer, sorry"
    
    query1 = str(query1)
    return query1

def OpenAI(query):
    
    # Set the API key
    openai.api_key = "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" #"YOUR_API_KEY"

    # Use the `Completion` endpoint to generate text
    model_engine = "text-davinci-002"
    prompt = query

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=  1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the generated text
    message = completion.choices[0].text
    return message
    # print(message)

while True:  
    Say(" okk nice mai tik hu or aap kese ho subhash ji")
    # query = Listen()
    # # print(query)

    # if 'goodbye' in query or 'bye' in query or 'Goodbye' in query:
    #     Say("Ok sir bye, you can call me any time")
    #     exit()  
    # else: 
    #     Say("okk nice, mai tik hu")
    #     # Say(OpenAI(query= query))


