import tkinter as tk

win = tk.Tk()
win.title("Máy tính")
win.geometry("400x500")

a_entry2 = tk.Entry(win, width=30, font=("Arial", 14))
a_entry2.pack(padx=10, pady=10, fill=tk.X)


# Hàm xử lý sự kiện khi nhấn các nút số và toán tử
def button_click(button_text):
    # Lấy nội dung hiện tại của entry2
    current = a_entry2.get()

    if button_text == "=":
        # Xử lý phép tính và hiển thị kết quả trên entry1 và entry2
        expression = current
        try:
            result = eval(expression)
            a_entry2.delete(0, tk.END)
            a_entry2.insert(tk.END, str(result))
        except Exception as e:
            a_entry2.delete(0, tk.END)
            a_entry2.insert(tk.END, "Error")
    elif button_text == "DEL":
        # Xóa ký tự cuối cùng trong entry2
        a_entry2.delete(0, tk.END)
    else:
        # Thêm nội dung của nút vào entry2
        a_entry2.insert(tk.END, button_text)


# Tạo Frame để chứa các nút và căn chúng về bên trái
frame_button1 = tk.Frame(win)
frame_button1.pack(padx=10, pady=10, fill=tk.X)
frame_button2 = tk.Frame(win)
frame_button2.pack(padx=10, pady=10, fill=tk.X)
frame_button3 = tk.Frame(win)
frame_button3.pack(padx=10, pady=10, fill=tk.X)
frame_button4 = tk.Frame(win)
frame_button4.pack(padx=10, pady=10, fill=tk.X)
frame_button5 = tk.Frame(win)
frame_button5.pack(padx=10, pady=10, fill=tk.X)

# Thiết lập các sự kiện cho các nút
a_delete = tk.Button(frame_button1, text="DEL", width=8, height=2, font=("Arial", 12), command=lambda: button_click("DEL"))
a_delete.pack(side=tk.LEFT, padx=5)
a_start = tk.Button(frame_button1, text="(", width=8, height=2, font=("Arial", 12), command=lambda: button_click("("))
a_start.pack(side=tk.LEFT, padx=5)
a_close = tk.Button(frame_button1, text=")", width=8, height=2, font=("Arial", 12), command=lambda: button_click(")"))
a_close.pack(side=tk.LEFT, padx=5)
a_percent = tk.Button(frame_button1, text="%", width=8, height=2, font=("Arial", 12), command=lambda: button_click("%"))
a_percent.pack(side=tk.LEFT, padx=5)

a_number7 = tk.Button(frame_button2, text="7", width=8, height=2, font=("Arial", 12), command=lambda: button_click("7"))
a_number7.pack(side=tk.LEFT, padx=5)
a_number8 = tk.Button(frame_button2, text="8", width=8, height=2, font=("Arial", 12), command=lambda: button_click("8"))
a_number8.pack(side=tk.LEFT, padx=5)
a_number9 = tk.Button(frame_button2, text="9", width=8, height=2, font=("Arial", 12), command=lambda: button_click("9"))
a_number9.pack(side=tk.LEFT, padx=5)
a_division = tk.Button(frame_button2, text=":", width=8, height=2, font=("Arial", 12), command=lambda: button_click("/"))
a_division.pack(side=tk.LEFT, padx=5)

a_number4 = tk.Button(frame_button3, text="4", width=8, height=2, font=("Arial", 12), command=lambda: button_click("4"))
a_number4.pack(side=tk.LEFT, padx=5)
a_number5 = tk.Button(frame_button3, text="5", width=8, height=2, font=("Arial", 12), command=lambda: button_click("5"))
a_number5.pack(side=tk.LEFT, padx=5)
a_number6 = tk.Button(frame_button3, text="6", width=8, height=2, font=("Arial", 12), command=lambda: button_click("6"))
a_number6.pack(side=tk.LEFT, padx=5)
a_mul = tk.Button(frame_button3, text="X", width=8, height=2, font=("Arial", 12), command=lambda: button_click("*"))
a_mul.pack(side=tk.LEFT, padx=5)

a_number1 = tk.Button(frame_button4, text="1", width=8, height=2, font=("Arial", 12), command=lambda: button_click("1"))
a_number1.pack(side=tk.LEFT, padx=5)
a_number2 = tk.Button(frame_button4, text="2", width=8, height=2, font=("Arial", 12), command=lambda: button_click("2"))
a_number2.pack(side=tk.LEFT, padx=5)
a_number3 = tk.Button(frame_button4, text="3", width=8, height=2, font=("Arial", 12), command=lambda: button_click("3"))
a_number3.pack(side=tk.LEFT, padx=5)
a_sub = tk.Button(frame_button4, text="-", width=8, height=2, font=("Arial", 12), command=lambda: button_click("-"))
a_sub.pack(side=tk.LEFT, padx=5)

a_number0 = tk.Button(frame_button5, text="0", width=8, height=2, font=("Arial", 12), command=lambda: button_click("0"))
a_number0.pack(side=tk.LEFT, padx=5)
a_dots = tk.Button(frame_button5, text=".", width=8, height=2, font=("Arial", 12), command=lambda: button_click("."))
a_dots.pack(side=tk.LEFT, padx=5)
a_isequalto = tk.Button(frame_button5, text="=", width=8, height=2, font=("Arial", 12), command=lambda: button_click("="))
a_isequalto.pack(side=tk.LEFT, padx=5)
a_plus = tk.Button(frame_button5, text="+", width=8, height=2, font=("Arial", 12), command=lambda: button_click("+"))
a_plus.pack(side=tk.LEFT, padx=5)

win.mainloop()
