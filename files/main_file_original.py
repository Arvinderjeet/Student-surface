print("aj tkinter")
from tkinter import *
##
tk= Tk()
tk.title("STUDENT SURFACE")
##Text.configure(font=("Times New Roman", 20, "italic"))
##(tkt,justify="center",command=, text = "", fg = "", padx="",pady="",bd="").place(x=30, y=50)

##def loginclicked():
##        tk.geometry("400x250")  
##        name = Label(tk, text = "Name")
##        name.place(x = 30,y = 50)
##        email = Label(tk, text = "Email")
##        email.place(x = 30, y = 75) 
##        password = Label(tk, text = "Password")
##        password.place(x = 30, y = 100)
##        e1 = Entry(tk)#.place(x = 80, y = 50)
##        e1.place(x = 80, y = 50)
##        e2 = Entry(tk)#.place(x = 80, y = 75)
##        e2.place(x = 80, y = 75)
##        e3 = Entry(tk)#.place(x = 95, y = 100)
##        e3.place(x = 95, y = 100)
##        submit = Button(tk,justify="center",command=back, text = "submit", fg = "blue", padx="4",pady="4",bd="2",font=("Times New Roman", 25, ""))
##        submit.place(x = 30, y = 130)
##        loginbutton.destroy()
def mainpage():
    tk.geometry("1360x760")
##submit = Button(tk, text = "Submit", command=mainpage).place(x = 30, y = 130)
def beginingindex():
    def back():
        tk.geometry("950x630")
        name.destroy()
        entryname.destroy()
        loginbutton.destroy()
        added.destroy()
        mainpage()
    tk.geometry("350x200")
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

tk.mainloop()

