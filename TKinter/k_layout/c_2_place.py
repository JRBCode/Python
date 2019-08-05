#
# c_2_place.py
# @author bulbasaur
# @description 
# @created 2019-07-28T17:47:37.687Z+08:00
# @last-modified 2019-07-28T17:57:34.139Z+08:00
#

from tkinter import *

root = Tk()

# relheight/relwidth 相对于父组件的大小（宽度/高度）
Label(root, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
Label(root, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
Label(root, bg="blue").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)

mainloop()
