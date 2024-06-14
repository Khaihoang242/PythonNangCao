import tkinter as tk

root = tk.Tk()

# Tạo một Button với width và height được tùy chỉnh
btn = tk.Button(root, text="Click Me", width=200, height=3)  # Width và height là số ký tự
btn.pack(padx=10, pady=10)

# Tạo một Button với phông chữ lớn hơn
btn_large_font = tk.Button(root, text="Click Me", font=("Helvetica", 16))  # Font size 16
btn_large_font.pack(padx=10, pady=10)
root.mainloop()