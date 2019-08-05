#
# tk_2.py
# @author bulbasaur
# @description 
# @created 2019-07-22T22:22:51.369Z+08:00
# @last-modified 2019-07-28T14:42:17.107Z+08:00
#

from tkinter import *

def callback():
    var.set("吹吧，我才不信呢~")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您所下载的影片含有\n未成年人限制内容，\n请满18周岁之后\n再点击观看！")
textLabel = Label(
    frame1, 
    textvariable=var, 
    justify=LEFT
)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="TKinter/b_picture/images/2_1.gif")
imageLabel = Label(frame1, image=photo)
imageLabel.pack(side=RIGHT)

theButton = Button(frame2, text="我已满18周岁", command=callback)
theButton.pack()

frame1.pack(padx=20, pady=30)
frame2.pack(padx=20, pady=30)

mainloop()