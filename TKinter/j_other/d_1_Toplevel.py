#
# d_Toplevel.py
# @author bulbasaur
# @description Toplevel 组件类似于 Frame 组件，
# 但Toplevel 组件是一个独立的顶级窗口，这种窗口
# 通常拥有标题栏、边框等部件
# 通常用在显示额外的窗口、对话框和其他弹出窗口上
# @created 2019-07-27T22:33:27.563Z+08:00
# @last-modified 2019-07-27T22:52:43.165Z+08:00
#

from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.title("FishC Demo")

    msg = Message(top, text="I love FishC.com")
    msg.pack()

# 连续点击可创建多个窗口
Button(root, text="创建顶级窗口", command=create).pack()

mainloop()
