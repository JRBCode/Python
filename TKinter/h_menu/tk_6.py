#
# tk_6.py
# @author bulbasaur
# @description 简单下拉列表的实现
# @created 2019-07-27T13:24:04.928Z+08:00
# @last-modified 2019-07-27T13:52:56.880Z+08:00
#

from tkinter import *

root = Tk()

variable1 = StringVar()
variable1.set("one")

w = OptionMenu(root, variable1, "one", "two", "three")
w.pack()

OPTIONS = [
    "California", 
    "458", 
    "FF", 
    "ENZO", 
    "LaFerrari"
]

variable2 = StringVar()
variable2.set(OPTIONS[0])

# 通过 * 来实现传递多个参数
w = OptionMenu(root, variable2, *OPTIONS)
w.pack()


mainloop()