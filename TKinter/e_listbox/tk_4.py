#
# tk_4.py
# @author bulbasaur
# @description 将用户通过滚动条选择的值输出到屏幕上
# @created 2019-07-23T23:26:08.095Z+08:00
# @last-modified 2019-07-23T23:31:35.637Z+08:00
#

from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=42)
s1.pack()

s2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)
s2.pack()

def show():
    print(s1.get(), s2.get())

Button(root, text="获取位置", command=show).pack()

mainloop()
