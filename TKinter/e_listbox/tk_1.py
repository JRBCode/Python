#
# tk_1.py
# @author bulbasaur
# @description 
# @created 2019-07-23T21:28:42.217Z+08:00
# @last-modified 2019-07-23T23:51:27.611Z+08:00
#

from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode=EXTENDED, height=2)
# height 
# 设置显示的行数
# selectmode
# selectmode=BROWSE    （默认），可通过拖动鼠标或方向键改变选项
# selectmode=SINGLE     鼠标拖动时选项不会跟着动
# selectmode=MULTIPLE   多选
# selectmode=EXTENDED   多选，但需要同时按住 Shift 或 Ctrl 键或拖动鼠标实现

theLB.pack()

LIST = ["鸡蛋","鸭蛋","鹅蛋","李狗蛋"]

for item in LIST:
    theLB.insert(END, item)

theButton = Button(master, text="删除它", \
    command=lambda x=theLB:x.delete(ACTIVE))

theButton.pack()

mainloop()
