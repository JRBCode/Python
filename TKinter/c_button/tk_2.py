#
# tk_6_2.py
# @author bulbasaur
# @description 
# @created 2019-07-23T16:48:47.194Z+08:00
# @last-modified 2019-07-23T17:02:29.374Z+08:00
#

from tkinter import *


root = Tk()

GIRLS = ['西施', '貂蝉', '王昭君', '杨玉环']

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)

mainloop()