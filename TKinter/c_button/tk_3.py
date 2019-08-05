#
# tk_3.py
# @author bulbasaur
# @description 
# @created 2019-07-23T17:28:35.422Z+08:00
# @last-modified 2019-07-23T17:44:04.108Z+08:00
#

from tkinter import *


root = Tk()

v = IntVar()

Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)
Radiobutton(root, text="Three", variable=v, value=3).pack(anchor=W)

mainloop()