#
# tk_8.py
# @author bulbasaur
# @description 撤销修改、删除
# @created 2019-07-26T20:13:56.451Z+08:00
# @last-modified 2019-07-26T20:43:10.293Z+08:00
#

from tkinter import *
import hashlib

root = Tk()

# 只设置 undo=True 一次性撤销插入或删除的所有字符
# 上一步基础上加上 autoseparators=False 后一次只撤销一个字符的修改
# 这个选项是让 Tkinter 在认为一次完整的操作结束后自动插入“分隔符”，然后绑定
# 键盘事件 callback，每次有输入就用 edit_separator() 方法人为地插入一个“分隔符”
text = Text(root, width=30, height=5, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT, "I love FishC.com!")

def callback(event):
    text.edit_separator()

text.bind('<Key>', callback)

def show():
    text.edit_undo()

Button(root, text="撤销", command=show).pack()

mainloop()