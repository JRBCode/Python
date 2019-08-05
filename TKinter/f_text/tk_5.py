#
# tk_2.py
# @author bulbasaur
# @description 用 tag_bind() 函数将文本与鼠标事件绑定
# @created 2019-07-26T17:41:58.309Z+08:00
# @last-modified 2019-07-26T20:09:52.102Z+08:00
#

from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")

text.tag_add("link", "1.7", "1.16")
text.tag_config("link", foreground="blue", underline=True)

# 鼠标样式切换为 arrow（箭头）形态
def show_arrow_cursor(event):
    text.config(cursor="arrow")

# 鼠标样式切换为 xterm（竖杠）形态
def show_xterm_cursor(event):
    text.config(cursor="xterm")
    
# 用默认浏览器打开指定网页
def click(event):
    webbrowser.open("http://www.fishc.com")

# <Enter> 鼠标进入文本时，调用函数 show_arrow_cursor
# <Leave> 鼠标离开文本时，调用函数 show_xterm_cursor
# <Button-1> 鼠标点击文本时，调用函数 click
text.tag_bind("link", "<Enter>", show_arrow_cursor)
text.tag_bind("link", "<Leave>", show_xterm_cursor)
text.tag_bind("link", "<Button-1>", click)


mainloop()