#
# tk_1.py
# @author bulbasaur
# @description Message: Label 的变体，
# 用于显示多行文本消息，能够自动换行，并
# 调整文本的尺寸使其适应给定的尺寸
# @created 2019-07-27T20:00:54.070Z+08:00
# @last-modified 2019-07-27T21:06:57.619Z+08:00
#

from tkinter import *

root = Tk()

w1 = Message(root, text="这是一则消息", width=100)
w1.pack()

w2 = Message(root, text="这是一则\n骇人听闻的长长长长长消息！", width=100)
w2.pack()

mainloop()
