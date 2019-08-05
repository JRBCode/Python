#
# tk_2.py
# @author bulbasaur
# @description 键盘响应，输出键盘输入的内容
# @created 2019-07-27T16:47:51.990Z+08:00
# @last-modified 2019-07-27T19:44:17.135Z+08:00
#

from tkinter import *

root = Tk()

def callback(event):
    # 输出键盘输入的字符
    # 只显示字母、数字、汉字
    # print(event.char)
    # 显示大部分按键，但汉字显示不出来
    print(event.keysym)

frame = Frame(root, width=300, height=300)
# 获得焦点后键盘输入事件才能响应
frame.bind("<Key>", callback)
# 获得焦点
frame.focus_set()
frame.pack()

mainloop()
