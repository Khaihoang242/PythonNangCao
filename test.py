import tkinter as tk

def action1():
    try:
        a = float(a_text1.get())
        b = float(a_text2.get())
        if a != 0:
            x = -b / a
            a_text3.delete(0, tk.END)
            a_text3.insert(0, str(x))
        else:
            a_text3.delete(0, tk.END)
            a_text3.insert(0, "Vo nghiem")
    except ValueError:
        a_text3.delete(0, tk.END)
        a_text3.insert(0, "Error")

def action2():
    a_text1.delete(0, tk.END)
    a_text2.delete(0, tk.END)
    a_text3.delete(0, tk.END)

win = tk.Tk()
win.title("Giai phuong trinh bac 1")
win.geometry("300x300")

frame_button1 = tk.Frame(win)
frame_button1.pack(padx=10, pady=10, fill=tk.X)
frame_button2 = tk.Frame(win)
frame_button2.pack(padx=10, pady=10, fill=tk.X)

label_a = tk.Label(frame_button1, text="a")
label_a.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
a_text1 = tk.Entry(frame_button1)
a_text1.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
a_button1 = tk.Button(frame_button1, text="Tinh", command=action1)
a_button1.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

label_b = tk.Label(frame_button1, text="b")
label_b.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
a_text2 = tk.Entry(frame_button1)
a_text2.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
a_button2 = tk.Button(frame_button1, text="Lam lai", command=action2)
a_button2.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

a_nghiem = tk.Label(frame_button2, text="Nghiem:")
a_nghiem.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
a_text3 = tk.Entry(frame_button2)
a_text3.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

win.mainloop()
