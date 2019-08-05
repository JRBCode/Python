#
# tk_2.py
# @author bulbasaur
# @description 在 Text 文本中插入 Button 按钮
# @created 2019-07-24T00:28:03.872Z+08:00
# @last-modified 2019-07-24T00:48:54.034Z+08:00
#

from tkinter import *

root = Tk()

text = Text(root, width=30,height=5)
text.pack()

text.insert(INSERT, "I love \n")
# INSERT 在光标所在位置插入内容

text.insert(END, "FishC.com!!!")

def show():
    print("呦，我帮我点了一下~")

b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()