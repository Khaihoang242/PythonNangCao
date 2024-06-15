import tkinter as tk
import math

def action1():
    try:
        a=float(text1.get())
        b=float(text2.get())
        c=float(text3.get())
        delta=float(b*b-(4*a*c))
        if delta<0:
            text4.delete(0, tk.END)
            text4.insert(0, "Pt vo nghiem")
        elif delta==0:
            x1=-b/(2*a)
            text4.delete(0, tk.END)
            text4.insert(0,str(x1) )
        else :
            x1=(-b+math.sqrt(delta))/2*a
            x2=(-b-math.sqrt(delta))/2*a
            text4.delete(0, tk.END)
            text4.insert(0,str(x1))
            text5.delete(0,tk.END)
            text5.insert(0, str(x2))
    except ValueError:
        text4.delete(0, tk.END)
        text4.insert(0, "Error")
        text5.delete(0, tk.END)
        text5.insert(0, "Error")
def action2():
    text1.delete(0,tk.END)
    text2.delete(0,tk.END)
    text3.delete(0,tk.END)
    text4.delete(0,tk.END)
    text5.delete(0,tk.END)
win=tk.Tk()
win.title("Giai pt bac 2")

frame1=tk.Frame(win)
frame1.pack(padx=10, pady=10, fill=tk.X)

frame2=tk.Frame(win)
frame2.pack(padx=10, pady=10, fill=tk.X)

label1=tk.Label(frame1, text="a")
label1.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)
text1=tk.Entry(frame1)
text1.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)
button1=tk.Button(frame1, text="Tinh",command=action1)
button1.grid(column=2, row=0, padx=10, pady=10, sticky=tk.W)

label2=tk.Label(frame1, text="b")
label2.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)
text2=tk.Entry(frame1)
text2.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10)
button2=tk.Button(frame1, text="DEL", command=action2)
button2.grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)

label3=tk.Label(frame1, text="c")
label3.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)
text3=tk.Entry(frame1)
text3.grid(column=1, row=3, sticky=tk.W, padx=10, pady=10)

label4=tk.Label(frame2, text="Nghiem 1:")
label4.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)
text4=tk.Entry(frame2)
text4.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)

label5=tk.Label(frame2, text="Nghiem 2:")
label5.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)
text5=tk.Entry(frame2)
text5.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10)


win.mainloop()
