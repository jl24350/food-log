import tkinter as tk
from pymongo import MongoClient
from usda import UsdaClient
import requests
import json
import time
import subprocess

def main_menu():
    window.destroy()
    subprocess.call("main.py", shell=True)

def log():
    author = author_entry.get().upper()
    food = food_entry.get().upper()
    date = date_entry.get().upper()

    try:
        params = {'api_key': 'mo6vfDLPRxpUz2lm6vmZZPpRafc7d2QCshx5AtWm'}
        data = {'generalSearchInput': food}
        response = requests.post(
            r'https://api.nal.usda.gov/fdc/v1/search',
            params=params,
             json=data
        )
        j = response.json()
        calories = j['foods'][0]['foodNutrients'][3]['value']

        client = MongoClient('localhost', 27017)
        db = client['food-log']
        collection = db['gui-log']
        doc = {"Author": author, "Food" : food, "Date" : date, "Calories": calories}
        collection.insert_one(doc)
        window.destroy()
        subprocess.call("success.py", shell=True)
    except:
        window.destroy()
        subprocess.call("failure.py", shell=True)

window = tk.Tk()
window.rowconfigure(0, minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)

title = tk.Label(master=window, text= "Fill in the information below",font=('Arial',25), background='DodgerBlue2').grid(row=0,column=0,columnspan=3,sticky="nsew",pady=50,padx=20)
    
author_label = tk.Label(master=window, text='Author',font=('Arial',15)).grid(row=1, column = 0)
author_entry = tk.Entry(master=window, width=30)
author_entry.grid(row=1, column = 1)

food_label = tk.Label(master=window, text='Food',font=('Arial',15)).grid(row=2, column = 0)
food_entry = tk.Entry(master=window, width=30)
food_entry.grid(row=2, column = 1)

date_label = tk.Label(master=window, text='Date',font=('Arial',15)).grid(row=3, column = 0)
date_entry = tk.Entry(master=window, width=30)
date_entry.grid(row=3, column = 1)

btn_enter =tk.Button(master=window, text="Log", command=log, width = 25,font=('Arial',12)).grid(row=4,column=1,pady=20)
btn_main_menu =tk.Button(master=window, text="Return to Main Menu", command=main_menu, width = 25,font=('Arial',12)).grid(row=4,column=2)
    
window.mainloop()