#
# c_2_PanedWindow.py
# @author bulbasaur
# @description 将窗口分为三部分，左边一部分，右边两部分
# @created 2019-07-27T22:09:58.910Z+08:00
# @last-modified 2019-07-27T22:14:48.905Z+08:00
#

from tkinter import *

# 水平分布
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

# orient=VERTICAL：设置为垂直分布，
m2 = PanedWindow(orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()
