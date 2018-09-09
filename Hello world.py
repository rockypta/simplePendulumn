from tkinter import *
import math 
import time

gui = Tk()
gui.geometry("1000x800")
c = Canvas(gui ,width=1000 ,height=800)
c.pack()

line1 = 150
line2 = 150
θ1 = math.pi/4
θ2 = math.pi/4

x1_cord = 500 + line1 * math.sin(θ1)
y1_cord = 30 + line1 * math.cos(θ1)
x2_cord = x1_cord + line2 * math.sin(θ2)
y2_cord = y1_cord + line2 * math.cos(θ2)

line_1 = c.create_line(500, 300, x1_cord, y1_cord, width=5, smooth="true")
line_2 = c.create_line(x1_cord, y1_cord, x2_cord, y2_cord, width=5, smooth="true")

oval1 = c.create_oval(x1_cord-15, y1_cord-15, x1_cord+15, y1_cord+15, fill = "black")
oval2 = c.create_oval(x2_cord-15, y2_cord-15, x2_cord+15, y2_cord+15, fill = "black")

g = 1
m1 = 10
m2 = 20
v2 = 0.0
v1 = 0.0




while 1:

    c.delete(line_1)
    c.delete(line_2)
    c.delete(oval1)
    c.delete(oval2)

    acc_len_seg1 = - g* (2*m1 + m2)*math.sin(θ1) - m2*g*math.sin(θ1 - 2*θ2)
    acc_len_seg1 -= 2*math.sin(θ1 - θ2) * m2*(v1*v1*line2 + v2*v2*line1*math.cos(θ1 - θ2))
    acc_len_seg1 /= line1*(2*m1 + m2 - m2*math.cos(2*θ1 - 2*θ2))

    acc_len_seg2 = 	2*math.sin(θ1 - θ2) 
    acc_len_seg2 *=  (v2*v2*line1*(m1 + m2) + g*(m1 + m2)*math.cos(θ1) + v1*v1*line2 * m2 *math.cos(θ1 - θ2))
    acc_len_seg2 /= line2* (2*m1 + m2 - m2*math.cos(2*θ1 - 2*θ2))


    θ1 += v2
    θ2 += v1

    v2 += acc_len_seg1
    v1 += acc_len_seg2


    prev_x2= x2_cord
    prev_y2 = y2_cord
    x1_cord = 500 + line1 * math.sin(θ1)
    y1_cord = 300 + line1 * math.cos(θ1)
    x2_cord = x1_cord + line2 * math.sin(θ2)
    y2_cord = y1_cord + line2 * math.cos(θ2)

    line_1 = c.create_line(500, 300, x1_cord, y1_cord, width=5, smooth="true")
    line_2 = c.create_line(x1_cord, y1_cord, x2_cord, y2_cord, width=5, smooth="true")

    oval1 = c.create_oval(x1_cord-15, y1_cord-15, x1_cord+15, y1_cord+15, fill = "black")
    oval2 = c.create_oval(x2_cord-15, y2_cord-15, x2_cord+15, y2_cord+15, fill = "black")

    path = c.create_line(prev_x2, prev_y2, x2_cord, y2_cord, width=2, smooth="true")

    gui.update()
    time.sleep(.01)

gui.update()
gui.title("First title")
gui.mainloop()
