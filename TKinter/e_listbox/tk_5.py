#
# tk_5.py
# @author bulbasaur
# @description 为滚动条选项设置选择步长和显示步长
# @created 2019-07-23T23:32:42.365Z+08:00
# @last-modified 2019-07-23T23:52:41.130Z+08:00
#resolution

from tkinter import *

root = Tk()

# tickinterval  设置显示步长，默认不显示
# resolution    设置选择步长（精度），默认值为 1
# length        设置滚动条显示的长度
Scale(root, from_=0, to=40, tickinterval=20, resolution=10, length=100).pack()
Scale(root, from_=0, to=200, tickinterval=20, resolution=5, length=400, orient=HORIZONTAL).pack() 

mainloop()