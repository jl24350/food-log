import tkinter as tk
from pymongo import MongoClient
import subprocess

def main_menu():
    window.destroy()
    subprocess.call("main.py", shell=True)

def delete():
    try:
        client = MongoClient('localhost', 27017)
        db = client['food-log']
        collection = db['gui-log']
        
        author_old = author_entry_old.get().upper()
        food_old = food_entry_old.get().upper()
        date_old = date_entry_old.get().upper()

        author_new = author_entry_new.get().upper()
        food_new = food_entry_new.get().upper()
        date_new = date_entry_new.get().upper()

        check = collection.find_one({"Author": author_old, "Food": food_old, "Date": date_old})
        if check.count() == 0:
            raise Exception()
        
        collection.update_one({"Author": author_old, "Food": food_old, "Date": date_old}, {"$set":{"Author": author_new, "Food": food_new, "Date": date_new}})
        window.destroy()
        subprocess.call("success.py", shell=True)
    except:
        window.destroy()
        subprocess.call("not-found.py", shell=True)

window = tk.Tk()
window.rowconfigure(0, minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)

title = tk.Label(master=window,text='Enter the old nd new information in each column',font=('Arial',20),background='DodgerBlue2').grid(row=0,column=0,columnspan=3,sticky="nsew",pady=50,padx=20)

old_label = tk.Label(master=window, text='Old',font=('Arial',15)).grid(row=1,column=1)
new_label = tk.Label(master=window, text='New',font=('Arial',15)).grid(row=1,column=2)

author_label = tk.Label(master=window, text='Author',font=('Arial',15)).grid(row=2, column = 0)
author_entry_old = tk.Entry(master=window, width=30)
author_entry_old.grid(row=2, column = 1,sticky='nesw',padx=15,pady=5)
author_entry_new = tk.Entry(master=window, width=30)
author_entry_new.grid(row=2, column = 2,sticky='nesw',padx=15,pady=5)

food_label = tk.Label(master=window, text='Food',font=('Arial',15)).grid(row=3, column = 0,sticky='nesw')
food_entry_old = tk.Entry(master=window, width=30)
food_entry_old.grid(row=3, column = 1,sticky='nesw',padx=15,pady=5)
food_entry_new = tk.Entry(master=window, width=30)
food_entry_new.grid(row=3, column = 2,sticky='nesw',padx=15,pady=5)

date_label = tk.Label(master=window, text='Date',font=('Arial',15)).grid(row=4, column = 0)
date_entry_old = tk.Entry(master=window, width=30,)
date_entry_old.grid(row=4, column = 1,sticky='nesw',padx=15,pady=5)
date_entry_new = tk.Entry(master=window, width=30)
date_entry_new.grid(row=4, column = 2,sticky='nesw',padx=15,pady=5)


btn_delete =tk.Button(master=window, text="Update", command=delete, width = 25,font=('Arial',12)).grid(row=5,column=1, pady=20)
btn_main_menu =tk.Button(master=window, text="Return to Main Menu", command=main_menu, width = 25,font=('Arial',12)).grid(row=5,column=2,pady=20)

window.mainloop()