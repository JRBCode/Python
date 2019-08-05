#
# c_PanedWindow.py
# @author bulbasaur
# @description PanedWindow 组件是一个空间管理组件，
# 跟 Frame 组件类似，都是为组件提供一个框架，不过
# PanedWindow 允许让用户调整应用程序的空间划分，会
# 为每一个子组件生成一个独立的窗格，
# 用户可以自由地调整窗格的大小
# @created 2019-07-27T21:43:34.488Z+08:00
# @last-modified 2019-07-27T22:16:01.880Z+08:00
#

from tkinter import *

# orient=VERTICAL：设置为垂直分布，
# 默认为水平分布
m = PanedWindow(orient=VERTICAL)
# fill=BOTH：设置此框架覆盖全局
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

mainloop()
