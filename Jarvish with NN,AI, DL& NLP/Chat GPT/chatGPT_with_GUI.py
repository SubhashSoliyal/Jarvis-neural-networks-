import tkinter as tk
import openai
import os

openai.api_key =os.environ.get( "OPENAI_API_KEY")

def send_message():
    # user_input = input_field.get()
    user_input = "hello"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt='User: ' + user_input + '\n\nChatGPT: ',
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    ).choices[0].text
    chat_history.config(state='normal')
    chat_history.insert('end', 'You: ' + user_input + '\n')
    chat_history.insert('end', 'ChatGPT: ' + response + '\n\n')
    chat_history.config(state='disabled')
    # input_field.delete(0, 'end')

root = tk.Tk()
root.title("ChatGPT")

frame = tk.Frame(root)

scrollbar = tk.Scrollbar(frame)
chat_history = tk.Text(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
chat_history.pack(side='left', fill='both', expand=True)
chat_history.config(state='disabled')
frame.pack()

# input_field = tk.Entry(root, width=50)
# input_field.pack(pady=10)

# send_button = tk.Button(root, text="Send", command=send_message)
# send_button.pack()

root.mainloop()
