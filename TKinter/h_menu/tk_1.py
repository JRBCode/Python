#
# tk_1.py
# @author bulbasaur
# @description 简单的菜单栏实现
# @created 2019-07-27T11:52:28.756Z+08:00
# @last-modified 2019-07-27T11:59:02.815Z+08:00
#

from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar = Menu(root)
menubar.add_command(label="hello", command=callback)
menubar.add_command(label="quit", command=root.quit)

root.config(menu=menubar)

mainloop()
