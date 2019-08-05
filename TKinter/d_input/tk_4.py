#
# tk_4.py
# @author bulbasaur
# @description 
# @created 2019-07-23T19:01:59.806Z+08:00
# @last-modified 2019-07-23T19:12:20.109Z+08:00
#


from tkinter import *

master = Tk()

# 鼠标从 e1 移到其他地方，调用 test() 函数

def test():
    if e1.get() == "小甲鱼":
        print("正确！")
        return True
    else:
        print("错误！")
        e1.delete(0, END)
        return False

v = StringVar()

e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=test)
e2 = Entry(master)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()
