import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import speech_recognition
import pyautogui

# Defining Frame
root = tk.Tk()
root.title("Let's talk")
root.geometry('1345x550+500+230')
root.resizable(False, False)
root.configure(bg='#04316F')
root.wm_iconbitmap('save.png')

# Listening Function
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        query  = r.recognize_google(audio,language='en-in')
        pyautogui.typewrite(query)
    except Exception as e:
        print("Say that again")
        return "None"
    return query

engine = pyttsx3.init()

# Speack Function
def speaknow():
    text = text_area.get(1.0, tk.END)
    gender = gender_combobox.get()
    seed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def set_voice():
        if (gender=='Male'):
            engine.setProperty('voice', voice[0].id)
            engine.say(text)
            engine.runAndWait()

        elif(gender=='Female'):
            engine.setProperty('voice', voice[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (seed=='Fast'):
            engine.setProperty('rate', 250)
            set_voice()
        elif (seed=='Normal'):
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 60)
            set_voice()            

# Download Function
def download():
    text = text_area.get(1.0, tk.END)
    gender = gender_combobox.get()
    seed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def set_voice():
        if (gender=='Male'):
            engine.setProperty('voice', voice[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

        elif(gender=='Female'):
            engine.setProperty('voice', voice[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (seed=='Fast'):
            engine.setProperty('rate', 250)
            set_voice()
        elif (seed=='Normal'):
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 60)
            set_voice()            


## save file
url = ''
def save_text(event=None):
    global url
    try:
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
    except:
        return

               
###############################################  TEXT TO SPEECH  ###########################################################

# Defining Text Area
text_area = tk.Text(root, font='Roboto 20 bold', bg='#2161B9', fg="#07ECF8", relief=tk.GROOVE, wrap=tk.WORD)
text_area.place(x=350, y=15, width=600, height=520)

# Hading
tk.Label(root, text='SPEECH TO TEXT', font="arial 20 bold", bg='#04316F', fg='#07ECF8').place(x=30, y=60)
tk.Label(root, text='TEXT TO SPEECH', font="arial 20 bold", bg='#04316F', fg='#07ECF8').place(x=990, y=60)

# Voice Gender
gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=970, y=150)
gender_combobox.set('Male')

# Voice Speed
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=1145, y=150)
speed_combobox.set('Normal')

# Speeck Button
btn = tk.Button(root, text='SPEECH', compound=tk.LEFT, width=10, font='arial 14 bold', bg='#2144F2', fg='#07ECF8', command=speaknow)
btn.place(x=975, y=270)

# Save Button
save = tk.Button(root, text='SAVE', compound=tk.LEFT, width=10, font='arial 14 bold', bg='#39c790', fg='red', command=download)
save.place(x=1145, y=270)

###########################################  END TEXT TO SPEECH  #############################################################


###########################################  SPEECH TO TEXT  #################################################################

# Start Button
btn = tk.Button(root, text='START', compound=tk.LEFT, width=19, font='arial 14 bold', bg='#04316F', fg='#07ECF8', command=takeCommand)
btn.place(x=30, y=150)

# Stop Button
save = tk.Button(root, text='SAVE AS TEXT FILE', compound=tk.LEFT, width=19, font='arial 14 bold', bg='#39c790', fg='red', command=save_text)
save.place(x=30, y=270)

root.mainloop()
