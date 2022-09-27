import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.geometry('300x150')


def dd():
      userInput="F:\\CODING\\._PYTHON\\text.py"
      print('│OPENING FILE |'+str(os.system(userInput)))

open_button = ttk.Button(
    root,
    text='Open a File',
    command=dd
    

)

open_button.pack(expand=True)


root.mainloop()
