import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tkinter Vars")
window.geometry("300x150")


def button_func():
    print(str_var.get())
    str_var.set("Button Pressed")

str_var = tk.StringVar()




label = ttk.Label( master = window, text = "label", textvariable = str_var )
label.pack()

entry = ttk.Entry( master = window, textvariable = str_var )
entry.pack()

button = ttk.Button( master = window, command = button_func )
button.pack()

window.mainloop()