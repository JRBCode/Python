#
# tk_4.py
# @author bulbasaur
# @description 
# @created 2019-07-23T00:29:43.853Z+08:00
# @last-modified 2019-07-28T14:42:06.822Z+08:00
#

from tkinter import *

root = Tk()


photo = PhotoImage(file="TKinter/b_picture/images/2_2.gif")
textLabel = Label(
    root, 
    text="Hello Everyone !!!\nHello,World!!! ", 
    justify=LEFT, 
    image=photo, 
    compound=CENTER, 
    font=("宋体", 20), 
    fg="black",
)

textLabel.pack(side=LEFT)

mainloop()