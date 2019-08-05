#
# b_grid.py
# @author bulbasaur
# @description 
# @created 2019-07-28T09:54:45.241Z+08:00
# @last-modified 2019-07-28T14:58:38.889Z+08:00
#

from tkinter import *

root = Tk()

# sticky=W 设置为左对齐
Label(root, text="用户名：").grid(row=0, sticky=W)
Label(root, text="密码：").grid(row=1, sticky=W)

photo = PhotoImage(file="Tkinter/k_layout/images/b_fishc.gif")
# rowspan=2 填充两行
Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx=40, pady=40)

Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

Button(text="提交", width=10).grid(row=2, columnspan=3, pady=20)

mainloop()
