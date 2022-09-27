from tkinter import *  
import time
##=====================================##
tk = Tk()  
tk.title("exiting programme (studentsurface)")
tk.resizable(0, 0)
tk.iconbitmap("F:\\CODING\\aj_singh\\ico\\student_surface_logo.ico")
def calc():
      userInput="F:\\CODING\\aj_singh\\main\\softind.py"
      print('│OPENING FILE |'+str(os.system(userInput)))

class beginingindex:
    tk.geometry("430x140+400+400")
    tk.resizable("false","false")

    exit_label = Label(tk,text="Thank you \u2764", fg="#231321", bd="0",font=("lucida calligraphy", 40, "bold"),padx="7", pady="3")
    exit_label.pack()

    exitbutton = Button(tk,justify="center",command=exit, text = "[exit]", bg = "red", padx="2",pady="2",bd="1",font=("Times New Roman", 15, "bold"))
    exitbutton.pack()

tk.mainloop()