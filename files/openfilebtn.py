from tkinter import *
from tkinter.messagebox import showinfo
import os
tk=Tk()
def dd():
      userInput="F:\\CODING\\._PYTHON\\text.py"
      print('│OPENING FILE |'+str(os.system(userInput)))
open_button = Button(
    tk,
    text='Open a File',
    command=dd
    )
open_button.pack()

tk.mainloop()