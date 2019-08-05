#
# tk_4.py
# @author bulbasaur
# @description 下拉菜单选中/取消、单选/多选
# @created 2019-07-27T12:52:39.633Z+08:00
# @last-modified 2019-07-27T13:00:12.212Z+08:00
#

from tkinter import *

root = Tk()

def callback():
    print("你好~")

menubar = Menu(root)

openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件", menu=filemenu)
filemenu.add_checkbutton(label="打开", command=callback, variable=openVar)
filemenu.add_checkbutton(label="保存", command=callback, variable=saveVar)
filemenu.add_separator()        # 添加分隔线
filemenu.add_checkbutton(label="退出", command=callback, variable=quitVar)

editVar = IntVar()

editmenu = Menu(menubar, tearoff=True)
menubar.add_cascade(label="编辑", menu=editmenu)
editmenu.add_radiobutton(label="剪切", command=callback, variable=editVar)
editmenu.add_radiobutton(label="拷贝", command=callback, variable=editVar)
editmenu.add_radiobutton(label="粘贴", command=callback, variable=editVar)

root.config(menu=menubar)

mainloop()