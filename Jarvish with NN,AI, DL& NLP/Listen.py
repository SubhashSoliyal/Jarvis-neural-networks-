import speech_recognition as  sr # pip install speechrecognition

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
        return query.lower()

    except:
         return '.'
    # query = str(query)
    # return query.lower()

Listen()
