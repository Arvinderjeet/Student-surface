from tkinter import *
import time
from tkinter.messagebox import showinfo
from tkinter import filedialog
import os
import webbrowser
import PyPDF2
# ===========BEGIN THE PROJECT ========= ======
tk= Tk()
tk.title("STUDENT SURFACE")
# tk=Toplevel()
tk.geometry("1360x760+0+0")
tk.iconbitmap("F:\\CODING\\aj_singh\\ico\\student_surface_logo.ico")
tk.configure(bg='#eeeeed')
def exit_button():
    userInput="F:\\CODING\\aj_singh\\main\\exit_button.py"
    print('│OPENING FILE |'+str(os.system(userInput)))
    time.sleep(1)
    exit()
copyright = Label(tk,text="made with \u2764 by Arvinderjeet Singh", font=("lucida calligraphy", 13, ""), bg=None, fg="#455443", bd="0")
copyright.place(x=460,y=705)
exitbutton = Button(tk,justify="center",command=exit_button, text = "[exit]", bg = "red", padx="2",pady="2",bd="1",font=("Times New Roman", 16, "bold"))
exitbutton.place(x=3,y=690)


# ============[clock]================

text_font= ("Boulder", 23, 'bold')
foreground= "#808080"
label_clock = Label(tk, font=text_font, bg=None, fg=foreground)
label_clock.place(x=1180, y=5)


def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label_clock.config(text=time_live) 
    label_clock.after(200, digital_clock)

digital_clock()

# canvas_logo_circle= Canvas(tk,width=400, height=400,bg=None)
# canvas_logo_circle.place(x=5,y=5)
# canvas_logo_circle.create_oval(13,13,210,210, width="2")

logo_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\student_surface_logo.png")
logo = Button(
    tk,
    text="logo",
    image = logo_img,
    bd="0"
    )
logo.image=logo_img
logo.place(x=50,y=-23)


canvas_left=Canvas(tk, width=250, height=560)
canvas_left.place(x=3,y=130)
canvas_left.create_rectangle(5, 5, 250, 560,outline="black",width="4",fill=None)

name = "Learner"
#=============[name]===============
user = Label(tk,text=f"HI! {name}\nWELCOME to the \n Student Surface ", font=("lucida calligraphy", 15, "bold"), bg=None, fg="#e938e7", bd="0")
user.place(x=15, y=170)

def calc():
      userInput="F:\\CODING\\aj_singh\\main\\calculator.py"
      print('│OPENING FILE |'+str(os.system(userInput)))

def board():
      userInput="F:\\CODING\\aj_singh\\main\\digital_board.py"
      print('│OPENING FILE |'+str(os.system(userInput)))

def ncert():
      userInput="F:\\CODING\\aj_singh\\main\\ncert.py"
      print('│OPENING FILE |'+str(os.system(userInput)))

def side_left():
    # ================CALCULATOR==========
    calc_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\calculator-logo.png")
    open_button_calc = Button(
        tk,
        text="calc",
        command=calc,
        image = calc_img,
        bd="0"
        )
    open_button_calc.image=calc_img
    open_button_calc.place(x=80,y=265)

    # ==============BOARD===============
    board_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\board_logo.png")
    open_button_board = Button(
        tk,
        text="board",
        command=board,
        image = board_img,
        bd="0"
        )
    open_button_board.image=board_img
    open_button_board.place(x=40,y=363)


    # =================line============
    canvas=Canvas(tk, width=10, height=700)
    canvas.place(x=260,y=5)
    canvas.create_line(2,2,2,700, fill="green", width=5)

    canvas2=Canvas(tk, width=10, height=700)
    canvas2.place(x=1060,y=5)
    canvas2.create_line(2,2,2,700, fill="green", width=5)
def pdf_viewer():
    text= Text(tk,width= 70,height=25,bg="#bffafd",font=("times New Roman", 15 , "bold"),wrap=WORD)
    def clear_text():
       text.delete(1.0, END)

    # def open_pdf():
    #    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    #    if file:
    #       pdf_file= PyPDF2.PdfFileReader(file)
    #       page= pdf_file.getPage(0)
    #       content=page.extractText()
    #       text.insert(1.0,content)

    def open_pdf():
        file = filedialog.askopenfilename(title="Select a PDF",initialdir="F:\\CODING\\aj_singh\\main\\ncert_pdf", filetype=(("PDF  Files","*.pdf"),("All Files","*.*")))
        if file:
            pdf_file=PyPDF2.PdfFileReader(file)
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
    open_file.place(x=960,y=50)


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
    clear_file.place(x=870,y=72)

    text.place(x=310,y=115)
    ncert_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\ncert_logo_main.png")
    open_button_ncert = Button(
        tk,
        text="ncert",
        command=ncert,
        image = ncert_img,
        bd="0"
        )
    open_button_ncert.image=ncert_img
    open_button_ncert.place(x=55,y=516)

label_heading=Label(tk, text = "Student Surface ", fg = "#505050", padx="0",pady="0",bd="0",font=("lucida calligraphy", 50, "bold"))
label_heading.place(x=310,y=5)
def right_side():
    label_platforms=Label(tk,justify="left", text = "Learn from\nOnline Platforms:", fg = "#333", padx="0",pady="0",bd="0",font=("sans serif", 12, "bold"))
    label_platforms.place(x=1085,y=90)

    canvas=Canvas(tk, width=250, height=700)
    canvas.place(x=1085,y=130)
    canvas.create_rectangle(5, 5, 186, 180,outline="black",width="4",fill=None)

    def pw():
        webbrowser.open_new(r"https://www.pw.live/")

    def vedantu():
        webbrowser.open_new(r"https://www.vedantu.com/")
    
    def unacademy():
        webbrowser.open_new(r"https://unacademy.com/")
    
    pw_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\pw_logo.png")
    pw_logo_btn = Button(tk,
                justify="center",
                command=pw,
                text = "physics wallah",
                fg = "blue",
                padx="0",pady="0",
                image = pw_logo,
                bd="0")
    pw_logo_btn.image=pw_logo
    pw_logo_btn.place(x=1092,y=249)

    vedantu_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\vedantu_logo.png")
    vedantu_logo_btn = Button(tk,
                justify="center",
                command=vedantu,
                text = "vedantu",
                fg = "blue",
                padx="0",pady="0",
                image = vedantu_logo,
                bd="0")
    vedantu_logo_btn.image=vedantu_logo
    vedantu_logo_btn.place(x=1092,y=192)

    unacademy_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\unacademy_logo.png")
    unacademy_logo_btn = Button(tk,
                justify="center",
                command=unacademy,
                text = "unacademy",
                fg = "blue",
                padx="0",pady="0",
                image = unacademy_logo,
                bd="0")
    unacademy_logo_btn.image=unacademy_logo
    unacademy_logo_btn.place(x=1092,y=137)


    # ============== skills ================
    label_skills=Label(tk,justify="left", text = "Learn from\nOnline skills:", fg = "#000", padx="0",pady="0",bd="0",font=("sans serif", 12, "bold"))
    label_skills.place(x=1085,y=350)

    canvas2=Canvas(tk, width=250, height=700)
    canvas2.place(x=1085,y=390)
    canvas2.create_rectangle(5, 5, 186, 180,outline="black",width="4",fill=None)

    def sololearn():
        webbrowser.open_new(r"https://www.sololearn.com/")

    def udemy():
        webbrowser.open_new(r"https://www.udemy.com/")
    
    def coursera():
        webbrowser.open_new(r"https://coursera.org/")

    def jnv_official():
        webbrowser.open_new(r"https://navodaya.gov.in/nvs/nvs-school/DODA/en/about_us/About-JNV/")

        # ============================================================
    def loc():
    	webbrowser.open_new(r"https://goo.gl/maps/g4JWkcWLVXKw6MLt9")
    # def contt():
    # 	webbrowser.open_new(r"https://navodaya.gov.in/nvs/nvs-school/DODA/en/about_us/About-JNV/")
    def mail():
    	webbrowser.open_new(r"https://navodaya.gov.in/nvs/nvs-school/DODA/en/about_us/About-JNV/")

    sololearn_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\sololearn_logo.png")
    sololearn_logo_btn = Button(tk,
                justify="center",
                command=sololearn,
                text = "physics wallah",
                fg = "blue",
                padx="0",pady="0",
                image = sololearn_logo,
                bd="0")
    sololearn_logo_btn.image=sololearn_logo
    sololearn_logo_btn.place(x=1092,y=509)

    udemy_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\udemy_logo.png")
    udemy_logo_btn = Button(tk,
                justify="center",
                command=udemy,
                text = "udemy",
                fg = "blue",
                padx="0",pady="0",
                image = udemy_logo,
                bd="0")
    udemy_logo_btn.image=udemy_logo
    udemy_logo_btn.place(x=1092,y=452)

    coursera_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\coursera_logo.png")
    coursera_logo_btn = Button(tk,
                justify="center",
                command=coursera,
                text = "coursera",
                fg = "blue",
                padx="0",pady="0",
                image = coursera_logo,
                bd="0")
    coursera_logo_btn.image=coursera_logo 
    coursera_logo_btn.place(x=1092,y=397)

    jnvdoda_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\jnv_logo.png")
    jnv_logo = Button(
        tk,
        text="logo",
        image = jnvdoda_logo,
        command=jnv_official,
        bd="0",
        fg = "blue",
        padx="0",pady="0"
        )
    jnv_logo.image=jnvdoda_logo
    jnv_logo.place(x=1092,y=620)

    # ================================

    loc_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\jnv_loc.png")
    logo_loc = Button(
        tk, 
        text="logo",
        image = loc_logo,
        command=loc,
        bd="0",
        padx="0",pady="0"
        )
    logo_loc.image=loc_logo
    logo_loc.place(x=1180,y=630)

    # =====================================

    # contt_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\jnv_contt.png")
    # logo_contt = Button(
    #     tk,
    #     text="logo",
    #     image = contt_logo,
    #     command=contt,
    #     bd="0",
    #     padx="0",pady="0"
    #     )
    # logo_contt.image=contt_logo
    # logo_contt.place(x=1205,y=630)

    # ===================================

    mail_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\jnv_mail.png")
    logo_mail = Button(
        tk,
        text="logo",
        image = mail_logo,
        command=mail,
        bd="0",
        padx="0",pady="0"
        )
    logo_mail.image=mail_logo
    logo_mail.place(x=1255,y=630)



right_side()
side_left()
pdf_viewer()
tk.mainloop()
