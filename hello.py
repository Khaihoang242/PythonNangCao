import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Frame Example")

# Tạo Frame
frame = tk.Frame(root)
frame.pack()

# Tạo button đầu tiên và đặt nó ở dòng đầu tiên
button1 = tk.Button(frame, text="Button 1")
button1.pack(side=tk.TOP, fill=tk.X)

# Tạo button thứ hai và đặt nó ở dòng thứ hai
button2 = tk.Button(frame, text="Button 2")
button2.pack( )

# Chạy vòng lặp chính
root.mainloop()
