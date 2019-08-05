#
# tk_3.py
# @author bulbasaur
# @description 在 Canvas 中绘制椭圆（圆）
# @created 2019-07-26T22:18:08.392Z+08:00
# @last-modified 2019-07-26T22:24:37.154Z+08:00
#

from tkinter import *

root = Tk()

w = Canvas(root, width=400, height=200, background="white")
w.pack()

w.create_rectangle(80, 40, 320, 160, dash=(4, 4))
w.create_oval(80, 40, 320, 160, fill="pink")
w.create_oval(140, 40, 260, 160, fill="yellow")
w.create_text(200, 100, text="FishC")

w.create_text(200, 100, text="FishC")

mainloop()
