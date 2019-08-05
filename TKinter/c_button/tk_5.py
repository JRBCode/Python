#
# tk_5.py
# @author bulbasaur
# @description 
# @created 2019-07-23T17:54:03.224Z+08:00
# @last-modified 2019-07-23T18:06:10.704Z+08:00
#

from tkinter import *


root = Tk()

group = LabelFrame(root, text="最好的脚本语言是？", padx=20, pady=30)
group.pack(padx=30,pady=30)

LANGS = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lua", 4)
]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()