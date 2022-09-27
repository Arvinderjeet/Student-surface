from tkinter import *
import time
print("aj tkinter")
##
tk= Tk()
tk.title("STUDENT SURFACE")
tk.geometry("1360x760+0+0")
def mainpage():
    tk.geometry("1360x760+0+0")
def beginingindex():
    def back():
        tk.geometry("950x630")
        name.destroy()
        entryname.destroy()
        loginbutton.destroy()
        added.destroy()
        mainpage()
    tk.geometry("350x200+0+0")
    tk.resizable("false","false")
    exitbutton = Button(tk,justify="center",command=exit, text = "[exit]", bg = "red", padx="2",pady="2",bd="1",font=("Times New Roman", 10, "bold"))
    exitbutton.grid(row = 0,column = 0)
    name = Label(tk, text = "Name", fg = "#505050", padx="5",pady="2",bd="0",font=("Times New Roman", 18, "bold"))
    name.grid(row = 1,column = 1)
    entryname = Entry(tk,width=30)
    entryname.grid(row = 1,column = 2)
    loginbutton = Button(tk,justify="center",command=back, text = "login", fg = "red", padx="5",pady="5",bd="0",font=("Times New Roman", 18, "italic"))
    loginbutton.grid(row = 4,column = 2)
    added = Label(tk, text = "already added:", fg = "#909090", padx="5",pady="20",bd="1",font=("Times New Roman", 13, "bold"))
    added.grid(row = 2, column = 1)
    
##    loginbutton.grid(row = 1,column = 1)

##    exitbutton = Button(tk,
beginingindex()
# tk = Tk() 
# tk.title("Digital Clock") 
# tk.geometry("420x150") 
# tk.resizable(1,1)

text_font= ("Boulder", 20, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 10

label = Label(tk, font=text_font, bg=None, fg=foreground, bd=border_width) 
label.place(x=1200, y= 30)


def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)


digital_clock()

tk.mainloop()

