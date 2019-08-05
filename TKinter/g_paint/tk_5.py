#
# tk_5.py
# @author bulbasaur
# @description 通过画小椭圆的方法实现用鼠标画图
# @created 2019-07-26T23:36:36.304Z+08:00
# @last-modified 2019-07-26T23:48:37.358Z+08:00
#

from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=400, height=300, background="white")
w.pack()

def paint(event):
    x1, y1 = (event.x - 1),(event.y - 1)
    x2, y2 = (event.x + 1),(event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill="red")

# 添加鼠标左键点击响应
w.bind("<B1-Motion>", paint)

Button(root, text="重新绘制", command=(lambda x=ALL:w.delete(x))).pack()

Label(root, text="按住鼠标左键并移动，开始你的理想蓝图吧......").pack(side=BOTTOM)

mainloop()
