#
# tk_4.py
# @author bulbasaur
# @description 初识 Tags，给指定文本设置样式
# @created 2019-07-26T17:08:08.619Z+08:00
# @last-modified 2019-07-26T20:09:36.632Z+08:00
#

from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")

text.tag_add("tag1", "1.7", "1.12", "1.14")

# background 指定背景颜色
# foreground 指定所选内容颜色
text.tag_config("tag1", background="yellow", foreground="red")

# 同一文本加多个 Tags,新创建的 Tags 样式会覆盖旧的 Tags 样式
# tag2 样式覆盖了 tag1 的样式
text.tag_add("tag2", "1.7", "1.12", "1.14")
text.tag_config("tag2", background="black", foreground="red")

# 设置 Tags 的优先级
# tag_raise()
# tag_lower()
text.tag_lower("tag2")

mainloop()
