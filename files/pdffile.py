import PyPDF2
from tkinter import *
from tkinter import filedialog

tk=Tk()
tk.geometry("500x500")
# text= Text(tk,width= 80,height=30)
# text.pack(pady=20)

text= Text(tk,width= 80,height=30,font=("times New Roman", 15 , "bold"),wrap=WORD)
def clear_text():
    text.delete(1.0, END)

def open_pdf():
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF     Files","*.pdf"),("All Files","*.*")))
    if file:
        pdf_file= PyPDF2.PdfFileReader(file)
        page= pdf_file.getPage(0)
        content=page.extractText()
        text.insert(1.0,content)
    
pdf_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\pdf_logo.png")
open_file = Button(tk,
                justify="center",
                command=open_pdf,
                text = "OPEN NEW FILE",
                fg = "blue",
                padx="0",pady="0",
                image = pdf_img,
                bd="0")
open_file.image=pdf_img
open_file.place(x=10,y=10)


clear_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\clear_btn.png")
clear_file = Button(tk,
                justify="center",
                command=clear_text,
                text = "clear",
                fg = "blue",
                padx="0",pady="0",
                image = clear_img,
                bd="0")

clear_file.image=clear_img
clear_file.place(x=60,y=10)

text.place(x=3,y=50)
tk.mainloop()