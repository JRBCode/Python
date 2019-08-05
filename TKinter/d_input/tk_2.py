#
# tk_2.py
# @author bulbasaur
# @description 
# @created 2019-07-23T18:13:40.785Z+08:00
# @last-modified 2019-07-23T18:36:53.007Z+08:00
#

from tkinter import *

root = Tk()

Label(root, text="作品：").grid(row=0, column=0)
Label(root, text="作者：").grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    if e1.get() == "" or e2.get() == "":
        print("输入信息不全 ！！！")
    else:
        print("作品：《%s》" % e1.get())
        print("作者：%s" % e2.get())
        e1.delete(0, END)
        e2.delete(0, END)

b1 = Button(root, text="获取信息", width=10, command=show)
b2 = Button(root, text="退出", width=10, command=root.quit)
b1.grid(row=3, column=0, sticky=W, padx=10, pady=5)
b2.grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()