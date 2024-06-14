import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("PythonGUI")
ttk.Label(win, text="A label").grid(column=0, row=0)
# ttk.Button( win , text="Button").grid(column=1,row=1)
ttk.Entry(win,).grid(column=1, row=1)
ttk.Combobox(win,).grid(column=1, row=2)
ttk.Treeview(win).grid(column=1, row=3)
win.mainloop()