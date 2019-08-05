#
# tk_7.py
# @author bulbasaur
# @description 简单的加法计算器
# @created 2019-07-23T20:27:25.635Z+08:00
# @last-modified 2019-07-26T20:08:17.810Z+08:00
#

from tkinter import *

master = Tk()

frame = Frame(master)
frame.pack(padx=30, pady=30)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

# 判断输入的内容是否为数字
def test(content):
    return content.isdigit()


testCMD = master.register(test)

e1 = Entry(
    frame, 
    width=15, 
    textvariable=v1, 
    validate="key", 
    # validate="key"：输入过程就进行判断，不满足条件就输入不进去
    validatecommand=(testCMD, '%P')
).grid(row=0, column=0)

Label(frame, text="+").grid(row=0, column=1)

e2 = Entry(
    frame, 
    width=15, 
    textvariable=v2, 
    validate="key", 
    validatecommand=(testCMD, '%P')
).grid(row=0, column=2)

Label(frame, text="=").grid(row=0, column=3)

e3 = Entry(
    frame, 
    width=15, 
    textvariable=v3, 
    state="readonly"
).grid(row=0, column=4)

def dele():
    v1.set("")
    v2.set("")

def calc():
    if v1.get() == "" or v2.get() == "":
        v3.set("输入信息不完整！")
    else:
        result = int(v1.get()) + int(v2.get())
        v3.set(result)

Button(frame, text="清空", command=dele).grid(row=1, column=0, pady=20)
Button(frame, text="计算结果", command=calc).grid(row=1, column=4, pady=20)

mainloop()