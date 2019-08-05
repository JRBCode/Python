#
# tk_1.py
# @author bulbasaur
# @description Spinbox：Entry 组件的变体，
# 用于从固定的值中选取一个
# @created 2019-07-27T21:19:30.951Z+08:00
# @last-modified 2019-07-27T21:39:04.115Z+08:00
#

from tkinter import *

root = Tk()

# increment：设置步长（精度），默认值为 1
# wrap：默认值为 False，为 True 时点上下箭头循环显示，
# 为 False 时向上点到 10 后再点向上的箭头数字不会变化
w1 = Spinbox(root, from_=0, to=10, increment=0.8, wrap=True)
w1.pack()

w2 = Spinbox(root, from_=0, to=10)
w2.pack()

OPTIONS = (
    "小甲鱼", 
    "~风介~", 
    "wei_Y", 
    "戴宇轩"
)

w3 = Spinbox(root, values=OPTIONS, wrap=True)
w3.pack()

mainloop()
