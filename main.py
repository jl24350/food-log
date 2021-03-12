import tkinter as tk
import subprocess

window = tk.Tk()

def delete():
    window.destroy()
    subprocess.call("delete-log.py", shell=True)

def list_logs():
    import list_logs

def log():
    window.destroy()
    subprocess.call("log.py", shell=True)

def update():
    window.destroy()
    subprocess.call("update.py", shell=True)


window.rowconfigure(0, minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)

lbl1 = tk.Label(master=window, text='Welcome to My Food Log', font=('Arial',25), background='DodgerBlue2').grid(row=0,column=0,columnspan=3,sticky="nsew",pady=50,padx=20)


log_button = tk.Button(master=window, text="Log a meal", command=log,font=('Arial',12)).grid(row=1, column=1, sticky="nsew", pady=10)
get_button = tk.Button(master=window, text="Get your entrys", command=list_logs,font=('Arial',12)).grid(row=2, column=1, sticky="nsew", pady=10)
update_button = tk.Button(master=window, text="Update an entry", command=update,font=('Arial',12)).grid(row=3, column=1, sticky="nsew", pady=10)
delete_button = tk.Button(master=window, text="Delete an entry", command=delete,font=('Arial',12)).grid(row=4, column=1, sticky="nsew",pady=10)

window.mainloop()