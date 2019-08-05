#
# tk_3.py
# @author bulbasaur
# @description 在 Text 文本中插入 Picture 图片
# @created 2019-07-24T00:35:07.587Z+08:00
# @last-modified 2019-07-28T14:40:26.487Z+08:00
#


from tkinter import *

root = Tk()

text = Text(root, width=45,height=50)
text.pack()

photo = PhotoImage(file="TKinter/f_text/images/3_fishc.gif")

def show():
    text.image_create(END, image=photo)

b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()
