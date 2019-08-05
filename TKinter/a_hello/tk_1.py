#
# tk_1.py
# @author bulbasaur
# @description 
# @created 2019-07-22T22:14:02.513Z+08:00
# @last-modified 2019-07-22T22:23:26.740Z+08:00
#

import tkinter as tk

app = tk.Tk()
app.title("FishC Demo")

theLabel = tk.Label(app, text="我的第二个窗口程序！")
theLabel.pack()

app.mainloop()