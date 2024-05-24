import tkinter as tk
from tkinter import ttk
import openai
import urllib.request
from PIL import Image as Ig
from PIL import ImageTk
from tkinter import *
import customtkinter
import os



openai.api_key = "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"

home = customtkinter.CTk()
home.title("Create Bot")
home.geometry("400x300")

# name of chat bot
name_entry = customtkinter.CTkEntry(home,placeholder_text = "Bot Name", width = 300,height = 30)
name_entry.place(x = 50 ,y =50)


# Write prompt for query from chat bot
objective_entry = customtkinter.CTkEntry(home,placeholder_text = "Define Use",width = 300,height=40)
objective_entry.place(x = 50 ,y =100)





def show_root():
    root.deiconify()
    name = name_entry.get()
    root.title(name)

    
open_root_button = customtkinter.CTkButton(home, text="Let's GO", command=show_root,corner_radius=0)
open_root_button.place(x = 200,y = 170)


# name = name_entry.get()
# objective = objective_entry.get()
# Function to correct code
def correct_code():
    # Get the code from the text box
    code = code_text.get("1.0", "end")
    objective = objective_entry.get()

    # Send the code to ChatGPT for correction
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= objective + "\n" + code,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the corrected code from the response
    corrected_code = response["choices"][0]["text"]

    # Clear the conversation box
    code_conversation.delete("1.0", "end")

    # Display the original code in the conversation box
    code_conversation.insert("1.0", "User: " + code, "red")

    # Display the corrected code in the conversation box
    code_conversation.insert("end", "Chatbot: " + corrected_code, "green")




# Create the main window
root = customtkinter.CTk()

#root.title(name)
root.geometry("640x540")

root.withdraw()

def clear_text():
    code_text.delete("1.0", END)

code_text = customtkinter.CTkTextbox(root, height=150, width=640)
code_text.pack(padx = 10,pady=10)

code_text.insert("1.0", "Write your Query here")

# Define a function to remove the background text
def remove_background_text(event):
    if code_text.get("1.0", "end-1c") == "":
        code_text.delete("1.0", "end")

# Bind the remove_background_text function to the <FocusIn> event of the code_text box
code_text.bind("<FocusIn>", remove_background_text)

code_button = customtkinter.CTkButton(root, text="Submit", command=lambda:[correct_code(),clear_text()])
code_button.pack()

# Create the conversation box for the code
code_conversation = customtkinter.CTkTextbox(root, height=320, width=640)
code_conversation.pack(padx =10,pady=10)

# Define the red and green text tags
code_conversation.tag_config("red", foreground="pink")
code_conversation.tag_config("green", foreground="yellow")

# Start the main event loop
home.mainloop()
