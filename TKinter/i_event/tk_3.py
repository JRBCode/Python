#
# tk_3.py
# @author bulbasaur
# @description 实时获得鼠标位置并在画布下方输出
# 鼠标移动时才会输出，静止时不输出
# @created 2019-07-27T16:58:35.540Z+08:00
# @last-modified 2019-07-27T19:30:20.321Z+08:00
#

from tkinter import *

root = Tk()

def callback(event):
    # 修改变量的值
    intVar1.set(event.x)
    intVar2.set(event.y)
    stringVar.set("当前位置：" + str(intVar1.get()) + " " + str(intVar2.get()))

frame = Frame(root, width=300, height=300)
# 添加鼠标移动事件，鼠标移动调用函数 callback()
frame.bind("<Motion>", callback)
frame.pack()

intVar1 = IntVar()
intVar2 = IntVar()
stringVar = StringVar()
intVar1.set(0)
intVar2.set(0)
stringVar.set("当前位置：" + str(intVar1.get()) + " " + str(intVar2.get()))

# 在底部输出鼠标实时位置
label = Label(root, textvariable=stringVar)
label.pack(side=BOTTOM)


mainloop()