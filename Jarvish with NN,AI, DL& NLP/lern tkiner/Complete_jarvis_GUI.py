from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import openai
import speech_recognition as sr
import pyttsx3 #pip install pyttsx3
import os



class JarvisOnline:
    
    def __init__(self,root) :
        self.root = root
        self.root.title('JARVIS')
        self.root.geometry('1000x700+0+0')
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root, bd= 3,bg='powder blue',width=600)
        main_frame.pack()


        img_jarvis = Image.open('D:\\vs_code\Jarvish with NN,AI, DL& NLP\lern tkiner\j.png')
        img_jarvis= img_jarvis.resize((200,70),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_jarvis)


        tital_label = Label(main_frame, bd=3, relief= RAISED, anchor= 'nw',
                            width=730,compound=LEFT, image=self.photoimg,
                            text='JARIVS',font=('arial',30,'bold'),fg='green',
                            bg= 'white')
        tital_label.pack(side= TOP)


        self.scroll_bar_y = ttk.Scrollbar(main_frame,orient= VERTICAL)
        self.text = Text(main_frame, width=65,height= 20, 
                         relief= RAISED,font=('arial',14),
                         yscrollcommand=self.scroll_bar_y.set)
        self.scroll_bar_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        # for button or text entry at lower
        btn_frame = Frame(self.root,bd=3, bg= 'white', width= 730)
        btn_frame.pack()

        self.ChatGPT_btn = Button(btn_frame, text='ChatGPT',
                                font=('arial',16,'bold'),width=8,
                                command=self.RUN, bg='green',fg='white')
        self.ChatGPT_btn.grid(row=0,column=0,padx=5,sticky=W)

        text_lable = Label(btn_frame,text='Type Something....',
                        font=('arial',14,'bold'),fg='green',
                        bg= 'white')
        text_lable.grid(row=1,column=0,padx=5,sticky=W)

        self.entry_box = StringVar()
        self.entry_box1 = ttk.Entry(btn_frame,textvariable=self.entry_box,width=30, font=('arial',17,'bold'))
        self.entry_box1.grid(row=1,column=1,padx=5,sticky=W)

        self.send_btn = Button(btn_frame, text='Send>>',
                                font=('arial',16,'bold'),width=8,
                                command=self.send_fun, bg='green',fg='white')
        self.send_btn.grid(row=1,column=2,padx=5,sticky=W)

        

        self.clear_btn = Button(btn_frame, text='Clear Data',
                                font=('arial',16,'bold'),width=8,
                                command=self.clear_text,bg='red',fg='white')
        self.clear_btn.grid(row=2,column=0,padx=5,sticky=W)

        self.msg = ''
        self.msg_lable = Label(btn_frame,text=self.msg,
                        font=('arial',14,'bold'),fg='red',
                        bg= 'white')
        self.msg_lable.grid(row=0,column=1,padx=5,sticky=W)


    ############################## FUNCTION DECLERETION ###########

    def enter_func(self,event):
        self.send_fun()
        self.entry_box.set('')
        
    def clear_text(self):
        self.text.delete('1.0',END)
        self.entry_box.set('')

    def Say(self, audio_in):
        self.audio_in = audio_in
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        self.engine.setProperty('rate',180)

        self.text.insert(END,'\n'+f"AI: {self.audio_in}")
        self.engine.say(text= audio_in)
        self.engine.runAndWait()

    def Listen(self):
        self.r = sr.Recognizer()

        with sr.Microphone() as source:
            self.msg = 'Listening.....'
            self.msg_lable.config(text= self.msg,bg='green')
            self.r.pause_threshold = 1
            self.audio = self.r.listen(source=source)
        try:
            self.msg = 'Recognizing.....'
            self.msg_lable.config(text= self.msg,bg='green')
            self.query = self.r.recognize_google(audio_data=self.audio,language='en-in')
            self.text.insert(END,'\n'+f"You Said: {self.query}")
            self.msg = ''
            self.msg_lable.config(text= self.msg,bg='green')

        except:
            pass
        return self.query


    def OpenAI(self,query):
        self.query = query
        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.response = openai.Completion.create(
            model="text-davinci-003",
            prompt= "\nAI:"+ self.query + "\nHuman:",
            # "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \nAI: I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific?\nHuman: \nAI: I'm happy to help in any way I can! What would you like assistance with?\nHuman: hello\nAI: Hi there! How can I help you today?\nHuman: wether\nAI: Are you looking for weather information? What city or region would you like to get a forecast for?\nHuman: good Are you looking for something good? I can help you with a variety of tasks such as providing information, completing tasks, and providing advice. Do you need any help with something specific? Is there a task I can help you with? Please let me know if there is anything I can do for you.",
            temperature=0.9,
            max_tokens=650,
            top_p=1,
            best_of=3,
            frequency_penalty=0.1,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        self.message = self.response["choices"][0]["text"]
        return self.message

    def RUN(self):
        while True:
                
            self.query = self.Listen()
            # self.text.insert(END,'\n\n'+'Bot: Hi')
            self.message=self.OpenAI(query= self.query)
            self.Say(audio_in= self.message)
            self.text.yview(END)


    def send_fun(self):

        send = '\t\t\t'+'You: '+ self.entry_box.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)


        if (self.entry_box.get() == ''):
            self.msg= 'Please enter some input'
            self.msg_lable.config(text= self.msg,fg='red')
        else:
            self.msg=''
            self.msg_lable.config(text= self.msg,fg='red')
        
        # convertiation start
        # text = which it show in bot massege 

        if (self.entry_box.get() == 'hello'):
            self.text.insert(END,'\n\n'+'AI: Hi')

        else:
            self.Say('you said:' + self.entry_box.get())
            self.massege_gain = self.OpenAI(self.entry_box.get())
            self.Say(self.massege_gain)
            # self.text.insert(END, '\n\n AI:'+ self.massege_gain)
            











if __name__ == '__main__':
    root = Tk()
    obj = JarvisOnline(root=root)
    root.mainloop()
