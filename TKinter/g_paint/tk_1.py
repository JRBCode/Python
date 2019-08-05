#
# tk_1.py
# @author bulbasaur
# @description 初识 Canvas 画布及移动、修改、删除某组件
# @created 2019-07-26T20:47:45.607Z+08:00
# @last-modified 2019-07-26T22:08:19.475Z+08:00
#

from tkinter import *

root = Tk()

w = Canvas(root, width=400, height=200, background="white")         # 画布
w.pack()

line1 = w.create_line(0, 100, 400, 100, fill="yellow")              # 直线
line2 = w.create_line(200, 0, 200, 200, fill="red", dash=(4, 4))    # 虚线
rect1 = w.create_rectangle(100, 50, 300, 150, fill="blue")          # 矩形

w.coords(line1, 0, 50, 400, 50)     # 移动直线的位置
w.itemconfig(rect1, fill="red")     # 修改各种选项
w.delete(line2)                     # 删除 line2

# 调用的函数有参数，用 lambda 表达式
Button(root, text="删除全部", command=(lambda x=ALL:w.delete(x))).pack()

mainloop()
