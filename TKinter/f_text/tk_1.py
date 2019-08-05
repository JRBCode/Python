#
# tk_1.py
# @author bulbasaur
# @description 一个简单的 Text 文本框
# @created 2019-07-24T00:21:18.915Z+08:00
# @last-modified 2019-07-24T00:27:45.791Z+08:00
#

from tkinter import *

root = Tk()

text = Text(root, width=20,height=3)
text.pack()

text.insert(INSERT, "I love \n")
# INSERT 在光标所在位置插入内容

text.insert(END, "FishC.com!!!")

mainloop()
