#
# d_2_Toplevel.py
# @author bulbasaur
# @description 
# @created 2019-07-27T22:56:22.718Z+08:00
# @last-modified 2019-07-27T23:05:48.965Z+08:00
#

from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    # -alpha：设置透明度
    top.attributes("-alpha", 0.6)
    top.title("FishC Demo")

    msg = Message(top, text="I love FishC.com")
    msg.pack()

# 连续点击可创建多个窗口
Button(root, text="创建顶级窗口", command=create).pack()

mainloop()
