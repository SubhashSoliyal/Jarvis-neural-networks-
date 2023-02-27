import pyttsx3 #pip install pyttsx3


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 175)

    print("    ")
    print(f"AI: {Text}")
    engine.say(text= Text)
    engine.runAndWait()
    print("    ")
Say("Hello bro")




