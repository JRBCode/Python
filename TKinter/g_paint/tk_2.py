#
# tk_2.py
# @author bulbasaur
# @description 在 Canvas 中添加文字
# @created 2019-07-26T22:08:36.820Z+08:00
# @last-modified 2019-07-26T22:16:29.022Z+08:00
#

from tkinter import *

root = Tk()

w = Canvas(root, width=400, height=200, background="white")
w.pack()

w.create_line(0, 0, 400, 200, fill="green", width=3)
w.create_line(400, 0, 0, 200, fill="green", width=3)
w.create_rectangle(80, 40, 320, 160, fill="green")
w.create_rectangle(130, 70, 270, 130, fill="yellow")

w.create_text(200, 100, text="FishC")

mainloop()
