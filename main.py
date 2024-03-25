import tkinter as tk
from tkinter import filedialog
import os
import pyttsx3
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to record the audio
def record_audio():
    with sr.Microphone() as source:
        print('listening...')
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print('Recognized: ', text)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.INSERT, text)
    except Exception as e:
        print('Error: ', e)

# Function to take command
def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio)
        print('Recognized: ', command)
        if command.lower() == 'stop':
            record_audio()
    except Exception as e:
        print('Error: ', e)

# Function to download the text
def download():
    global url
    if url:
        content = str(text_area.get(1.0, tk.END))
        with open(url, 'w', encoding='utf-8') as fw:
            fw.write(content)
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        content2 = text_area.get(1.0, tk.END)
        url.write(content2)
        url.close()

# Function to speak the text
def speaknow():
    global url
    text = text_area.get(1.0, tk.END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the text area
text_area = tk.Text(root, font='Roboto 20 bold', bg='#2161B9', fg="#07ECF8", relief=tk.GROOVE, wrap=tk.WORD)
text_area.place(x=350, y=15, width=600, height=520)

# Heading
tk.Label(root, text='SPEECH TO TEXT', font="arial 20 bold", bg='#04316F', fg='#07ECF8').place(x=30, y=60)
tk.Label(root, text='TEXT TO SPEECH', font="arial 20 bold", bg='#04316F', fg='#07ECF8').place(x=990, y=60)

# Start Button
btn = tk.Button(root, text='START', compound=tk.LEFT, width=19, font='arial 14 bold', bg='#04316F', fg='#07ECF8', command=takeCommand)
btn.place(x=30, y=150)

# Stop Button
save = tk.Button(root, text='STOP', compound=tk.LEFT, width=19, font='arial 14 bold', bg='#39c790', fg='red', command=record_audio)
save.place(x=30, y=270)

# Speech Button
btn = tk.Button(root, text='SPEECH', compound=tk.LEFT, width=10, font='arial 14 bold', bg='#2144F2', fg='#07ECF8', command=speaknow)
btn.place(x=975, y=270)

# Save Button
save= tk.Button(root, text='SAVE', compound=tk.LEFT, width=10, font='arial 14 bold', bg='#39c790', fg='red', command=download)
save.place(x=1145, y=270)

# Mainloop
root.mainloop()