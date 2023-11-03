import tkinter as tk
from tkinter import ttk

def button_func():
    text_entry = entry.get()

    #update label
    label["text"] = text_entry
    entry["state"] = "disabled"
    #label["textColor"] = "red"
    #print(label.configure())
    
def reset_func():
    label["text"] = "Some Text"
    entry["state"] = "enabled"


window = tk.Tk()
window.title("Getting and setting widgets")

#widgets

label = ttk.Label(master = window, text = "Some Text")
label.pack()

entry = ttk.Entry(master= window)
entry.pack()


button1 = ttk.Button(master= window, text = "The button", command= button_func)
button1.pack()

reset_button = ttk.Button(master= window, text = "Reset", command= reset_func)
reset_button.pack()





#run
window.mainloop()

