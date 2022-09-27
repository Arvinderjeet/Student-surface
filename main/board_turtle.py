from turtle import *
import tkinter

t = Turtle()
t.shape=("turtle")
sc = Screen()
# sc.setup(400, 300)
# t.hideturtle()

t.color("red")
def coor(x, y):
	t.ondrag(None)
	t.setheading(t.towards(x,y))
	t.goto(x,y)
	t.ondrag(coor)
# t.fd(188)
# coor(3,5)
onscreenclick(coor)
print(onscreenclick(coor))
sc.mainloop()
