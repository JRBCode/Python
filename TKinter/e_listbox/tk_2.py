#
# tk_2.py
# @author bulbasaur
# @description 通过滚动条来显示 0~999 
# @created 2019-07-23T23:08:28.487Z+08:00
# @last-modified 2019-07-23T23:25:12.243Z+08:00
#

from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, i)

lb.pack(side=LEFT, fill=BOTH)

sb.config(command=lb.yview)

mainloop()
