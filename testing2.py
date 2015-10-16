import tkinter
from tkinter import *

Tk = tkinter.Tk
self=Tk()
listbox = Listbox(self, width = 10, height = 60)
listbox.grid(row =0, column=0)
scrollbar = Scrollbar(self)
scrollbar.grid(sticky=E, row = 0, rowspan = 100, column = 11, ipady = 1000)
mainloop()