#
# c_colorchooser.py
# @author bulbasaur
# @description 颜色选择对话框
# @created 2019-07-28T21:06:23.731Z+08:00
# @last-modified 2019-07-28T21:08:50.806Z+08:00
#

from tkinter import colorchooser
from tkinter import *

root = Tk()

def callback():
    fileName = colorchooser.askcolor()
    print(fileName)

Button(root, text="选择颜色", command=callback).pack()

mainloop()