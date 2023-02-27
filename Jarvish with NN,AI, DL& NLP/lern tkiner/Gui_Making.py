import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Jarvis Online')

# pack() method:It organizes the widgets in blocks before placing in the parent widget.
# grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
# place() method:It organizes the widgets by placing them on specific positions directed by the programmer.

button = tkinter.Button(root, text= 'Exit', width= 25, command= root.destroy)
button.pack()

# activebackground: to set the background color when button is under the cursor.
# activeforeground: to set the foreground color when button is under the cursor.
# bg: to set the normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the button.
# width: to set the width of the button.
# height: to set the height of the button.

canvas = Canvas(root, width = 40, height = 60)
canvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)

# w = Canvas(master, option=value)
# master is the parameter used to represent the parent window.
# bd: to set the border width in pixels.
# bg: to set the normal background color.
# cursor: to set the cursor used in the canvas.
# highlightcolor: to set the color shown in the focus highlight.
# width: to set the width of the widget.
# height: to set the height of the widget.


var1 = IntVar()
Checkbutton(root, text= 'male', variable= var1).pack() #.grid(row = 20, column = 1)
var2 = IntVar()
Checkbutton(root, text= 'female', variable= var2).pack() #.grid(row = 22, column = 1)


# w = CheckButton(master, option=value)
# Title: To set the title of the widget.
# activebackground: to set the background color when widget is under the cursor.
# activeforeground: to set the foreground color when widget is under the cursor.
# bg: to set the normal backgrouSteganography
# Break

# Secret Code:

# Attach a File:nd color.

# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the widget.
e1= Entry(root)
e2= Entry(root)
Label(root, text='First Name').pack()#grid(row= 1)
Label(root, text='Last Name').pack()# grid(row =2)

e1.pack() #e1.griad(row = 1, column = 2)
e2.pack() #e2.griad(row = 2, column = 2) 


# Entry:It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used.
# The general syntax is:
# w=Entry(master, option=value)
# bd: to set the border width in pixels.
# bg: to set the normal background color.
# cursor: to set the cursor used.
# command: to call a function.
# highlightcolor: to set the color shown in the focus highlight.
# width: to set the width of the button.
# height: to set the height of the button.



frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)
redbutton = Button(frame, text = 'Red', fg = 'red')
redbutton.pack(side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)


# Label: It refers to the display box where you can put any text or image which can be updated any time as per the code.
# The general syntax is:
# w=Label(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# bg: to set the normal background color.
# bg to set the normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the button.
# width: to set the width of the button.
# height” to set the height of the button.

w = Label(root, text= 'GreeksForGreeks.org!').pack()


# Listbox: It offers a list to the user from which the user can accept any number of options.
# The general syntax is:

# w = Listbox(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# bg: to set the normal background color.
# bd: to set the border width in pixels.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

lb = Listbox(root)
lb.insert(1, 'Python')
lb.insert(2, 'Java')
lb.insert(3, 'C++')
lb.insert(4, 'Any other')
lb.pack()


# MenuButton: It is a part of top-down menu which stays on the window all the time. Every menubutton has its own functionality. The general syntax is:
# w = MenuButton(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# activebackground: To set the background when mouse is over the widget.
# activeforeground: To set the foreground when mouse is over the widget.
# bg: to set the normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.
# highlightcolor: To set the color of the focus highlight when widget has to be focused.

mb = Menubutton (root, text= 'GFG')
mb.pack()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
cVar  = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()


# Menu: It is used to create all kinds of menus used by the application.
# The general syntax is:
# w = Menu(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# title: To set the title of the widget.
# activebackground: to set the background color when widget is under the cursor.
# activeforeground: to set the foreground color when widget is under the cursor.
# bg: to set the normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the widget.
# from tkinter import *
      

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')




# Message: It refers to the multi-line and non-editable text. It works same as that of Label.
# The general syntax is:
# w = Message(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# bd: to set the border around the indicator.
# bg: to set the normal background color.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

ourMessage = 'This is our Message'
messageVer = Message(root, text = ourMessage)
messageVer.config(bg = 'lightGreen')
messageVer.pack()


# RadioButton: It is used to offer multi-choice option to the user. It offers several options to the user and the user has to choose one option.
# The general syntax is:
# w = RadioButton(master, option=value)
# There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# activebackground: to set the background color when widget is under the cursor.
# activeforeground: to set the foreground color when widget is under the cursor.
# bg: to set the normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the label in characters.
# height: to set the height of the label in characters.

v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)

# Scale: It is used to provide a graphical slider that allows to select any value from that scale. The general syntax is:
# w = Scale(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# cursor: To change the cursor pattern when the mouse is over the widget.
# activebackground: To set the background of the widget when mouse is over the widget.
# bg: to set the normal background color.
# orient: Set it to HORIZONTAL or VERTICAL according to the requirement.
# from_: To set the value of one end of the scale range.
# to: To set the value of the other end of the scale range.
# image: to set the image on the widget.
# width: to set the width of the widget.

scale = Scale(root, from_=0, to= 42)
scale.pack()
scale= Scale(root, from_=0, to= 200, orient= HORIZONTAL)
scale.pack()

# Scrollbar: It refers to the slide controller which will be used to implement listed widgets.
# The general syntax is:
# w = Scrollbar(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# width: to set the width of the widget.
# activebackground: To set the background when mouse is over the widget.
# bg: to set the normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.

scrollbar = Scrollbar(root)
scrollbar.pack( side= RIGHT, fill= Y)
myList = Listbox(root, yscrollcommand= scrollbar.set)
for line in range(100):
    myList.insert(END, 'This is line number' + str(line))
myList.pack(side= LEFT, fill= BOTH)
scrollbar.config(command= myList.yview)

# Text: To edit a multi-line text and format the way it has to be displayed.
# The general syntax is:
# w  =Text(master, option=value)
# There are number of options which are used to change the format of the text. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# insertbackground: To set the background of the widget.
# bg: to set the normal background color.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

T = Text(root, height= 2, width= 30)
T.pack()
T.insert(END, "Greeks FOr Black\nBest Website\n")


# TopLevel: This widget is directly controlled by the window manager. It don’t need any parent window to work on.The general syntax is:
# w = TopLevel(master, option=value)
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# bg: to set the normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# width: to set the width of the widget.
# height: to set the height of the widget.

root.title('GFG')
top = Toplevel()
top.title("Python")

# SpinBox: It is an entry of ‘Entry’ widget. Here, value can be input by selecting a fixed value of numbers.The general syntax is:
# w = SpinBox(master, option=value)
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# bg: to set the normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# command: To call a function.
# width: to set the width of the widget.
# activebackground: To set the background when mouse is over the widget.
# disabledbackground: To disable the background when mouse is over the widget.
# from_: To set the value of one end of the range.
# to: To set the value of the other end of the range.

SpinBOx = Spinbox(root, from_= 0, to = 10)
SpinBOx.pack()

# PannedWindowIt is a container widget which is used to handle number of panes arranged in it. The general syntax is:
# w = PannedWindow(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

# bg: to set the normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# width: to set the width of the widget.
# height: to set the height of the widget.

m1 = PanedWindow()
m1.pack(fill= BOTH, expand= 1)
left = Entry(m1, bd= 5)
m1.add(left)
m2 = PanedWindow(m1, orient= VERTICAL)
m1.add(m2)
top = Scale(m2, orient= HORIZONTAL)
m2.add(top)


root.mainloop()