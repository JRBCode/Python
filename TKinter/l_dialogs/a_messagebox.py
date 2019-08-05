#
# a_messagebox.py
# @author bulbasaur
# @description 用 mssagebox 弹出对话框
# 点击确定返回 True；点击取消返回 False
# @created 2019-07-28T19:36:49.579Z+08:00
# @last-modified 2019-07-28T20:31:46.955Z+08:00
#

from tkinter import *
from tkinter import messagebox

root = Tk()

label = Label(root, width=50, height=10)
label.pack()

def callback():
    print(messagebox.askokcancel(parent=label, \
        title="FishC Demo", message="发射核弹？"))

button = Button(root, text="弹出对话框", width=15, \
    height=3, bg="black", fg="white", command=callback)
button.place(relx=0.5, rely=0.5, anchor=CENTER)


mainloop()
