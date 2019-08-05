#
# b_filedialog.py
# @author bulbasaur
# @description 用 filedialog 选择电脑里面的文件
# @created 2019-07-28T20:35:36.633Z+08:00
# @last-modified 2019-07-28T21:02:45.363Z+08:00
#
from tkinter import *
from tkinter import filedialog

root = Tk()

def callback1():
    # defaultextension 指定文件的后缀，当用户输入一个文件名
    # “FishC” 的时候,文件名会自动添加后缀为 “FishC.py”，
    # 如果用户输入的文件名包含后缀，那么该选项不生效
    fileName = filedialog.askopenfilename(defaultextension=".py")
    print(fileName)

Button(root, text="打开文件", command=callback1).pack()


def callback2():
    # filetypes 指定筛选文件类型的下拉菜单选项，
    # 该选项的值是由 2 元组构成的列表
    # 每个 2 元组由（类型名，后缀）构成
    fileName = filedialog.askopenfilename(filetypes=[("PNG", ".png"), \
        ("GIF", ".gif"), ("JPG", ".jpg"), ("Python", ".py")])
    print(fileName)

Button(root, text="打开文件", command=callback2).pack()

mainloop()
