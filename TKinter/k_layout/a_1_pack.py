#
# tk_1.py
# @author bulbasaur
# @description 
# @created 2019-07-28T09:00:29.391Z+08:00
# @last-modified 2019-07-28T09:16:15.156Z+08:00
#

from tkinter import *

root = Tk()

listbox = Listbox(root)
# fill=BOTH：listbox 组件填充 root 组件
# expand=True：当用户拉伸窗口时，listbox
# 组件跟着变化
listbox.pack(fill=BOTH, expand=True)

for i in range(10):
    listbox.insert(END, str(i))

mainloop()
