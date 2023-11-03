import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print("the button was pressed")
    
def button_func2():
    print("hello")
#create window
window = ttk.Window(themename = "journal")
window.title("Cool")
window.geometry("800x500")

#ttk widgets
label = ttk.Label(master=window,text="this is a test")
label.pack()

#create widgets
text = tk.Text(master=window)
text.pack()

#ttk entry 
entry = ttk.Entry(master=window)
entry.pack()

#My label
label = ttk.Label(master=window,text="My label")
label.pack()

#ttk button
button = ttk.Button(master=window, text="a Buttton", command=button_func)
button.pack()

#My button
button = ttk.Button(master=window, text="hello", command=lambda: print("hello"))
#button = ttk.Button(master=window, text="hello", command=button_func2)
button.pack()

#run
window.mainloop()
