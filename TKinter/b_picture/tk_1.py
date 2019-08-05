#
# tk_3.py
# @author bulbasaur
# @description 
# @created 2019-07-22T22:47:13.093Z+08:00
# @last-modified 2019-07-28T14:41:58.154Z+08:00
#

from tkinter import *

root = Tk()

textLabel = Label(
    root, 
    text="您所下载的影片含有\n未成年人限制内容，\n请满18周岁之后\n再点击观看！", 
    justify=LEFT, 
    padx=60
)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="TKinter/b_picture/images/2_1.gif")
imageLabel = Label(root, image=photo)
imageLabel.pack(side=RIGHT)

mainloop()