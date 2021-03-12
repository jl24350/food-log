import tkinter as tk
import time
import subprocess

def main_menu():
    window.destroy()
    subprocess.call("main.py", shell=True)

window = tk.Tk()
window.rowconfigure(0, minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)

title = tk.Label(master=window, text= "Something Went Wrong! Try Again",font=('Arial',30))
title.grid(row=0, column = 1)

btn_enter =tk.Button(master=window, text="Return to Main Menu", command=main_menu, width = 25,font=('Arial',12))
btn_enter.grid(row=2,column=1,pady=10)


window.mainloop()

