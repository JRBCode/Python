#
# tk_3.py
# @author bulbasaur
# @description 指定范围的选项（通过滚动条来选择）
# @created 2019-07-23T23:19:40.605Z+08:00
# @last-modified 2019-07-23T23:24:07.376Z+08:00
#

from tkinter import *

root = Tk()

Scale(root, from_=0, to=42).pack()
Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()
# orient 设置为水平方向

mainloop()
