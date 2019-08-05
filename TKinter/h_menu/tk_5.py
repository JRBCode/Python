#
# tk_5.py
# @author bulbasaur
# @description 在画布的任意位置添加下拉菜单按钮
# @created 2019-07-27T13:09:51.581Z+08:00
# @last-modified 2019-07-27T13:21:15.865Z+08:00
#

from tkinter import *

root = Tk()

def callback():
    print("你好~")

# relief 设置按钮样式
mb = Menubutton(root, text="点我", relief=RAISED)
mb.pack()

filemenu = Menu(mb, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()        # 添加分隔线
filemenu.add_command(label="退出", command=root.quit)

mb.config(menu=filemenu)

mainloop()