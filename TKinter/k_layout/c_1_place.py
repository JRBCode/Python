#
# c_place.py
# @author bulbasaur
# @description 
# @created 2019-07-28T15:00:29.176Z+08:00
# @last-modified 2019-07-28T17:58:50.468Z+08:00
#

from tkinter import *

root = Tk()

photo = PhotoImage(file="Tkinter/k_layout/images/c_logo.gif")
Label(root, image=photo).pack()

def callback():
    print("正中靶心！")

# Button 的位置会随着用户拉伸屏幕而发生变化
# relx rely 相对于父组件的水平/垂直位置，0 为最左/上端，1 为最下/右端
Button(root, text="点我", width=15, height=3, command=callback)\
.place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
