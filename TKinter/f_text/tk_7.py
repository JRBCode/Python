#
# tk_7.py
# @author bulbasaur
# @description 在文本中查找指定内容
# 注：将 start 指向下一个位置：start = pos + "+1c"
# @created 2019-07-26T19:30:58.828Z+08:00
# @last-modified 2019-07-27T16:52:50.217Z+08:00
#

from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")

# 将 line.column 形式的 index 值以元组的形式返回
def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))

start = "1.0"

while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print("找到了，位置是：", getIndex(text, pos))
    # 直接输出也可以
    # print("找到了，位置是：", pos)
    # 将 start 指向下一个位置
    start = pos + "+1c"


mainloop()