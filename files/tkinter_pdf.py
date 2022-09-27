from tkPDFViewer import tkPDFViewer as pdf
from tkinter import*
root = Tk()
page_pixmap = page.get_pixmap(
        matrix=fitz.Matrix(1.0, 1.0),
        clip=True,
    )
#create object like this.
variable1 = pdf.ShowPdf()
#Add your pdf location and width and height.
variable2 = variable1.pdf_view(root,pdf_location=r"F:\\PDFs\\TO PRINT\\www-javatpoint-com-python-built-in-functions.pdf",width=50,height=100)
variable2.pack()
root.mainloop()