#
# tk_6.py
# @author bulbasaur
# @description 
# @created 2019-07-23T20:10:34.340Z+08:00
# @last-modified 2019-07-23T20:27:49.576Z+08:00
#

from tkinter import *

master = Tk()
v = StringVar()

def test(content, reason, name):
    if content == "小甲鱼":
        print("正确！")
        print(content, reason, name)
        return True
    else:
        print("错误！")
        print(content, reason, name)
        return False

testCMD = master.register(test)
e1 = Entry(
    master, 
    textvariable=v, 
    validate="focusout", 
    validatecommand=(testCMD, '%P', '%v', '%W')
)
e2 = Entry(master)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()
