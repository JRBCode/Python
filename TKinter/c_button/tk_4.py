#
# tk_4.py
# @author bulbasaur
# @description 
# @created 2019-07-23T17:44:50.634Z+08:00
# @last-modified 2019-07-23T17:51:05.770Z+08:00
#

from tkinter import *


root = Tk()

LANGS = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lua", 4)
]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
    b.pack(fill=X)

mainloop()