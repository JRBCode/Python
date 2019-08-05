#
# tk_2.py
# @author bulbasaur
# @description 简单下拉菜单栏的实现
# @created 2019-07-27T11:59:20.174Z+08:00
# @last-modified 2019-07-27T12:32:47.386Z+08:00
#

from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar = Menu(root)

# tearoff 默认值为 True，点击编辑，出现的下拉菜单栏
# 第一行会多一条虚线，点击该虚线，下拉菜单栏选项会在
# 另外一个窗口打开，用户也可以在新出现的窗口操作
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件", menu=filemenu)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()        # 添加分隔线
filemenu.add_command(label="退出", command=root.quit)

editmenu = Menu(menubar, tearoff=True)
menubar.add_cascade(label="编辑", menu=editmenu)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="粘贴", command=root.quit)

root.config(menu=menubar)

mainloop()