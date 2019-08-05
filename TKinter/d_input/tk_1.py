#
# tk_1.py
# @author bulbasaur
# @description 
# @created 2019-07-23T18:09:20.239Z+08:00
# @last-modified 2019-07-23T18:12:47.920Z+08:00
#

from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx=20,pady=20)

e.delete(0, END)
e.insert(0,"默认文本...")

mainloop()
