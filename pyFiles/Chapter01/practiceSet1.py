# Multi lines string

print(''' 
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      This is my first program in Python!
      ''')

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, I am Agentic AI. What Can I help you today?")
engine.runAndWait()


import os

# Provide the specific directory path
directory_path = "/"

# OS module helps to list down all the directory path
contents = os.listdir(directory_path)
print("Contents: ",contents)

