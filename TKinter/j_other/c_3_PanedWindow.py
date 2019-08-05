#
# c_3_PanedWindow.py
# @author bulbasaur
# @description 将各部分之间的分割线显示出来
# @created 2019-07-27T22:17:43.782Z+08:00
# @last-modified 2019-07-27T23:00:48.579Z+08:00
#

from tkinter import *

# showhandle=True：手柄
# handlepad：手柄位置（距离最左端或最上端的像素），默认为 8
# handlesize：设置手柄大小，默认值为 8
# sashrelief=SUNKEN：设置分割线样式（下凹），
# 默认样式与背景重叠
m1 = PanedWindow(showhandle=True, handlepad=30, handlesize=15, sashrelief=SUNKEN)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

# orient=VERTICAL：设置为垂直分布，
m2 = PanedWindow(orient=VERTICAL, sashrelief=SUNKEN)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()
