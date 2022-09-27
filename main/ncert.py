import PyPDF2
from tkinter import *
from tkinter import filedialog
import pyttsx3
import threading

tk=Tk()
tk.geometry("880x680+460+40")
tk.title("BOOKS Reader")
tk.iconbitmap("F:\\CODING\\aj_singh\\ico\\ncert_logo_main.ico")
tk.resizable(0, 0)

if __name__ == "__main__":

	def home():
		userInput="F:\\CODING\\aj_singh\\main\\softind.py"
		print('│OPENING FILE |'+str(os.system(userInput)))

	# "F:\CODING\aj_singh\main\softind.py"

	logo_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\student_surface_logo.png")
	logo = Button(
		tk,
		text="logo",
		image = logo_img,
		bd="0",
		command=home
		)
	logo.image=logo_img
	logo.place(x=727,y=5 )
	text= Text(tk,width= 70,height=25,bg="#bffafd",font=("times New Roman", 15 , "bold"),wrap=WORD)
	label_heading= Label(tk,text="PDF Viewer (ncert) \u2764", fg="#0e0", bd="0",font=("lucida calligraphy", 30, "bold"), pady="0")
	label_heading.place(x=50,y=10)
	def clear_text():
	   text.delete(1.0, END)
	file=""
	def open_pdf():
		file = filedialog.askopenfilename(title="Select a PDF",initialdir="F:\\CODING\\aj_singh\\main\\ncert_pdf", filetype=(("PDF	Files","*.pdf"),("All Files","*.*")))
		if file:
			pdf_file=PyPDF2.PdfFileReader(file)
			page= pdf_file.getPage(0)
			content=page.extractText()
			text.insert(1.0,content)
			def readaloud():
			# book =  open("F:\\PDFs\\TO PRINT\\Python-Set-Methods-Cheat-Sheet.20210604.pdf", 'rb')
			# book=file
			# pdfReader = PyPDF2.PdfFileReader(book)
			# paged = pdfReader.numPages
			# print(paged)
				speak = pyttsx3.init()
				# from_page = pdfReader.getPage(0)
				# text = from_page.extractText()
				speak.say(content)
				speak.runAndWait()
			def rr():
				v = threading.Thread(target=readaloud, daemon=True)
				v.start()
			read_logo = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\read_logo.png")

			read = Button(tk,
				justify="center",
				command=rr,
				# command=readaloud,
				text = "read",
				fg = "blue",
				padx="0",pady="0",
				font=("lucida calligraphy", 50, "bold"),
				image = read_logo,
				bd="0")
			read.image=read_logo
			read.place(x=720,y=500)

	pdf_img = PhotoImage(file = r"F:\\CODING\\aj_singh\\logo\\pdf_logo.png")

	open_file = Button(tk, text="Read aloud",
				fg = "blue",
				padx="0",pady="0",
				image = pdf_img,
				bd="0",
				command=open_pdf
				)

	open_file.image=pdf_img
	open_file.place(x=720,y=160)
	open_file = Button(tk,
				justify="center",
				command=open_pdf,
				text = "OPEN NEW FILE",
				fg = "blue",
				padx="0",pady="0",
				image = pdf_img,
				bd="0")
	# print(content)
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
	clear_file.place(x=630,y=20)

	text.place(x=5,y=65)
tk.mainloop()