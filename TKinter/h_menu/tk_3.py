#
# tk_3.py
# @author bulbasaur
# @description 单击鼠标右键在鼠标箭头处弹出菜单
# @created 2019-07-27T12:16:02.558Z+08:00
# @last-modified 2019-07-27T16:36:26.824Z+08:00
#

from tkinter import *

root = Tk()

def callback():
    print("撤销/重做~")

menubar = Menu(root, tearoff=False)
menubar.add_command(label="撤销", command=callback)
menubar.add_command(label="重做", command=root.quit)

frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    # x_root/y_root 相对于屏幕的位置
    menubar.post(event.x_root, event.y_root)

# 添加单击鼠标右键响应事件
frame.bind("<Button-3>", popup)

mainloop()