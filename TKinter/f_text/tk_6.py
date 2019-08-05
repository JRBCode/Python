#
# tk_6.py
# @author bulbasaur
# @description 用 MD5 判断文本内容是否发生改变
# @created 2019-07-26T18:18:25.595Z+08:00
# @last-modified 2019-07-26T20:05:46.863Z+08:00
#


from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")
# 获得文本内容
contents = text.get("1.0", END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    # 获得点击按钮时文本内容
    contents = text.get("1.0", END)
    if sig != getSig(contents):
        print("警报，内容发生变动！！！")
    else:
        print("风平浪静~")

Button(root, text="检查", command=check).pack()

mainloop()