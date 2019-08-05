#
# tk_6.py
# @author bulbasaur
# @description 
# @created 2019-07-23T16:38:07.940Z+08:00
# @last-modified 2019-07-23T16:47:36.138Z+08:00
#

from tkinter import *


root = Tk()

v = IntVar()

c = Checkbutton(root, text="测试一下", variable=v)
c.pack()

l = Label(root, textvariable=v)
l.pack()

mainloop()
