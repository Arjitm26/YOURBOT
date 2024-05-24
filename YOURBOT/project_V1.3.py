import tkinter as tk
from tkinter import ttk
import openai
import urllib.request
from PIL import Image as Ig
from PIL import ImageTk
from tkinter import *
import customtkinter
import os





# Define the API key for the OpenAI API
openai.api_key = "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"



# Function to correct code
def correct_code():
    # Get the code from the text box
    code = code_text.get("1.0", "end")

    # Send the code to ChatGPT for correction
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Please correct the following Python code:\n" + code,
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

# Function to generate image
def generate_image():
    # Get the prompt from the text box
    prompt = image_text.get("1.0", "end")

    # Send the prompt to DALL-E for image generation
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        size="1024x1024",
        n=1,
        response_format="url",
    )

    # Get the generated image URL from the response
    image_url = response["data"][0]["url"]

    # Clear the conversation box
    image_conversation.delete("1.0", "end")

    # Display the prompt in the conversation box
    image_conversation.insert("1.0", "User: " + prompt, "red")

    # Display the generated image URL in the conversation box
    image_conversation.insert("end", "Chatbot: " + image_url, "green")
    
    #display the image from the url.

    urllib.request.urlretrieve(image_url,"result")
    #img = ImageTk.PhotoImage(Image.open("result"))
    img = Ig.open("result")
    img.show()


#Function to generate text
def generate_text():
    # Get the prompt from the text box
    prompt = text_text.get("1.0", "end")

    # Send the prompt to GPT-3 for text generation
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the generated text from the response
    generated_text = response["choices"][0]["text"]

    # Clear the conversation box
    text_conversation.delete("1.0", "end")

    # Display the prompt in the conversation box
    text_conversation.insert("1.0", "User: " + prompt, "red")

    # Display the generated text in the conversation box
    
    text_conversation.insert("end", "Chatbot: " + generated_text, "green")





home = customtkinter.CTk()
home.title("Home Page")
home.geometry("640x480")




# Add a background image
img = PhotoImage(file = "main_window.png")

background_label = tk.Label(home, image=img)
background_label.place(x=0,y=0)

def show_root():
    root.deiconify()
    
open_root_button = customtkinter.CTkButton(home, text="Open Application", command=show_root,corner_radius=0)
open_root_button.place(x = 450,y = 360)

def open_file():
    os.startfile("Mentor Form Major 2 Group30.pdf")

label1 = tk.Label(home,text="ChatBots using OpenAI APIs", font=("Times new roman", 30),bg = 'white')
label1.pack(pady = 50)

help1_button = customtkinter.CTkButton(home,text = "Documentation",corner_radius=0,command = open_file)
help1_button.place(x = 450 , y = 390)

help_button = customtkinter.CTkButton(home,text = "Create Bot (Beta)",corner_radius=0,command = open_file,fg_color = 'grey',hover_color = 'Black')
help_button.place(x = 450 , y = 421)
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("850x680")
root.configure(bg='grey')

root.withdraw()






customtkinter.set_default_color_theme("dark-blue")

# Create the tabs
tabs = ttk.Notebook(root)

# Create the Code Correction tab
code_tab = ttk.Frame(tabs)
tabs.add(code_tab, text="Code Correction")

#Create the text box for the code
code_text = customtkinter.CTkTextbox(code_tab, height=150, width=640)
code_text.pack(padx = 5,pady=5)

# method to clear the chat box once submit is pressed for new input

def clear_text():
    code_text.delete("1.0", END)

# Create the button to submit the code
code_button = customtkinter.CTkButton(code_tab, text="Submit", command=lambda:[correct_code(),clear_text()])
code_button.pack()

# Create the conversation box for the code
code_conversation = customtkinter.CTkTextbox(code_tab, height=320, width=640)
code_conversation.pack(padx = 5,pady=5)

# Define the red and green text tags
code_conversation.tag_config("red", foreground="pink")
code_conversation.tag_config("green", foreground="yellow")



# Create the Image Generation tab
image_tab = ttk.Frame(tabs)
tabs.add(image_tab, text="Image Generation")

#Create the text box for the code
image_text = customtkinter.CTkTextbox(image_tab, height=150, width=640)
image_text.pack(padx = 5,pady=5)

# Create the button to submit the code
image_button = customtkinter.CTkButton(image_tab, text="Submit", command=generate_image)
image_button.pack()

# Create the conversation box for the code
image_conversation = customtkinter.CTkTextbox(image_tab,  height=320, width=640)
image_conversation.pack(padx = 5,pady=5)

# Define the red and green text tags
image_conversation.tag_config("red", foreground="pink")
image_conversation.tag_config("green", foreground="green")


# Create the Code Correction tab
text_tab = ttk.Frame(tabs)
tabs.add(text_tab, text="Text Generation")

#Create the text box for the code
text_text = customtkinter.CTkTextbox(text_tab,height=150, width=640)
text_text.pack(padx = 5,pady=5)

# Create the button to submit the code
text_button = customtkinter.CTkButton(text_tab, text="Submit", command=generate_text)
text_button.pack()

# Create the conversation box for the code
text_conversation = customtkinter.CTkTextbox(text_tab,  height=320, width=640)
text_conversation.pack(padx = 5,pady=5)

# Define the red and green text tags
text_conversation.tag_config("red", foreground="pink")
text_conversation.tag_config("green", foreground="green")



tabs.pack(padx = 10,pady=30)





home.mainloop()


