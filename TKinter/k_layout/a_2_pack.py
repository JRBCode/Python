#
# a_2_pack.py
# @author bulbasaur
# @description 
# @created 2019-07-28T09:17:18.412Z+08:00
# @last-modified 2019-07-28T09:34:49.284Z+08:00
#

from tkinter import *

root = Tk()

frame1 = Frame(root)
frame1.pack(fill=X, side=TOP)

# fg：字体颜色；fill=X：三个 Label 都横向填充
Label(frame1, text="red", bg="red", fg="white").pack(fill=X)
Label(frame1, text="green", bg="green", fg="black").pack(fill=X)
Label(frame1, text="blue", bg="blue", fg="white").pack(fill=X)


frame2 = Frame(root)
frame2.pack(fill=X, side=BOTTOM)

# 三个 Label 横向排列
Label(frame2, width=10, text="red", bg="red", fg="white").pack(side=LEFT)
Label(frame2, width=10, text="green", bg="green", fg="black").pack(side=LEFT)
Label(frame2, width=10, text="blue", bg="blue", fg="white").pack(side=LEFT)


mainloop()
