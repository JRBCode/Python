#
# tk_4.py
# @author bulbasaur
# @description 画五角星
# @created 2019-07-26T22:27:44.810Z+08:00
# @last-modified 2019-07-26T23:08:08.061Z+08:00
#

from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=400, height=300, background="blue")
w.pack()

center_x = 200      # 中心点 x 坐标
center_y = 150      # 中心点 y 坐标
r = 100             # 中心点到顶点的距离

points = [
    # 左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 左下点
    center_x - int(r * m.cos(3 * m.pi / 10)),
    center_y + int(r * m.sin(3 * m.pi / 10)),
    # 中上点
    center_x,
    center_y - r,
    # 右下点
    center_x + int(r * m.cos(3 * m.pi / 10)),
    center_y + int(r * m.sin(3 * m.pi / 10)),
]

w.create_polygon(points, outline="green", fill="yellow")

mainloop()
