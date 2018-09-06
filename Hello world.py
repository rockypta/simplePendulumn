from tkinter import *
import time
import math
gui = Tk()
gui.geometry("800x800")
c = Canvas(gui ,width=800 ,height=800)
c.pack()

len_seg1 = 170
len_seg2 = 200
first_angle = 0.0
sec_angle = 0.0

x1_cord = 400 + len_seg1 * math.sin(first_angle)
y1_cord = 30 + len_seg1 * math.cos(first_angle)
x2_cord = x1_cord + len_seg2 * math.sin(sec_angle)
y2_cord = y1_cord + len_seg2 * math.cos(sec_angle)

line1 = c.create_line(400, 30, x1_cord, y1_cord, width=5, smooth="true")
line2 = c.create_line(x1_cord, y1_cord, x2_cord, y2_cord, width=5, smooth="true")

oval1 = c.create_oval(x1_cord-15, y1_cord-15, x1_cord+15, y1_cord+15, fill = "black")
oval2 = c.create_oval(x2_cord-15, y2_cord-15, x2_cord+15, y2_cord+15, fill = "black")


while 1:
    first_angle +=  0.01
    gui.update()


gui.update()
gui.title("First title")
gui.mainloop()
