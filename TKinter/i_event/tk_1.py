#
# tk-1.py
# @author bulbasaur
# @description 鼠标响应事件
# <Button-1> 鼠标左键
# <Button-2> 鼠标滚轮
# <Button-3> 鼠标右键
# @created 2019-07-27T16:36:40.238Z+08:00
# @last-modified 2019-07-27T16:47:27.311Z+08:00
#

from tkinter import *

root = Tk()

def callback(event):
    # 输出鼠标所在位置坐标（相对于画布左上角）
    print("点击位置：", event.x, event.y)

frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", callback)
frame.pack()

mainloop()
