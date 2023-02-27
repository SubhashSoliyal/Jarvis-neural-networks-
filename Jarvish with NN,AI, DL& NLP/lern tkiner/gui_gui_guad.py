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

        text_lable = Label(btn_frame,text='Type Something....',
                        font=('arial',14,'bold'),fg='green',
                        bg= 'white')
        text_lable.grid(row=0,column=0,padx=5,sticky=W)

        self.entry_box = StringVar()
        self.entry_box1 = ttk.Entry(btn_frame,textvariable=self.entry_box,width=30, font=('arial',17,'bold'))
        self.entry_box1.grid(row=0,column=1,padx=5,sticky=W)

        self.send_btn = Button(btn_frame, text='Send>>',
                                font=('arial',16,'bold'),width=8,
                                command=self.send_fun, bg='green',fg='white')
        self.send_btn.grid(row=0,column=2,padx=5,sticky=W)

        self.clear_btn = Button(btn_frame, text='Clear Data',
                                font=('arial',16,'bold'),width=8,
                                command=self.clear_text,bg='red',fg='white')
        self.clear_btn.grid(row=1,column=1,padx=5,sticky=W)

        self.msg = ''
        self.msg_lable = Label(btn_frame,text=self.msg,
                        font=('arial',14,'bold'),fg='red',
                        bg= 'white')
        self.msg_lable.grid(row=2,column=1,padx=5,sticky=W)


    ############################## FUNCTION DECLERETION ###########

    def enter_func(self,event):
        self.send_fun()
        self.entry_box.set('')
        
    def clear_text(self):
        self.text.delete('1.0',END)
        self.entry_box.set('')

  



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
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry_box.get() == 'hi'):
            self.text.insert(END,'\n\n'+'Bot: Hi sir')

        else:
            self.text.insert(END, '\n\n'+"BOt: sorry I diden't get it")






if __name__ == '__main__':
    root = Tk()
    obj = JarvisOnline(root=root)
    root.mainloop()
