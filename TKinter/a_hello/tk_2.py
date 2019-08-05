#
# tk_2.py
# @author bulbasaur
# @description 
# @created 2019-07-22T22:22:51.369Z+08:00
# @last-modified 2019-07-23T18:16:06.429Z+08:00
#

import tkinter as tk

class APP:
    def __init__(self, master):
        frame  = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=50, pady=30)

        self.hi_there = tk.Button(frame, text="打招呼", bg="black", fg="white", command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("Hello World !!!")


root = tk.Tk()
app = APP(root)

root.mainloop()
