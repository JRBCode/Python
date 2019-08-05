#
# saolei.py
# @author bulbasaur
# @description 
# @created 2019-07-29T13:26:59.950Z+08:00
# @last-modified 2019-07-29T15:53:37.491Z+08:00
#

from tkinter import *


root = Tk()

ROW = 20
COLUMN = 20
BOMB = 20

v = {}
for r in range(ROW):
    num = {}
    for c in range(COLUMN):
        num[c] = IntVar()
    v[r] = num


def callback():
    v[0][1].set(1)

for r in range(ROW):
    for c in range(COLUMN):
        b = Checkbutton(root, text=str(r)+"."+str(c), variable=v[r][c], \
            fg="white", width=3, indicatoron=False, command=callback)
        b.grid(row=r, column=c)

mainloop()