# digital_oard.py
from tkinter import *

# ================================
tk = Tk()
tk.geometry("820x650+530+50")
tk.title( "Digital Board" )
tk.resizable(0, 0)  
tk.iconbitmap("F:\\CODING\\aj_singh\\ico\\board_icon.ico")
colors_list = [ 'white' ,"BLACK", 'red' , 'green' , 'blue' , 'cyan' , 'yellow' , 'magenta']
menu= StringVar()
menu.set("white")
colors = OptionMenu(tk, menu, *colors_list)
colors.pack(side=TOP)
menu.set(menu.get())
# pen_color = menu.get()
# ================================
def clear():
   w.delete("all")
# ================================
# ====================
button_clear = Button(tk,text="CLEAR",command=clear,fg="red",font=("times new roman", 15, "bold"))
button_clear.pack(side=TOP)
# ====================
canvas_width = 800
canvas_height = 550
def paint( event ):
   x1, y1 = ( event.x - 5 ), ( event.y - 5 )
   x2, y2 = ( event.x + 5 ), ( event.y + 5 )
   global drawing
   drawing = w.create_oval( x1, y1, x2, y2, fill = menu.get() , width = 0 ) #PEN_COLOR
w = Canvas(tk, 
           width=canvas_width,
           bg="black",
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
message = Label( tk, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()