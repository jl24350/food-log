import tkinter as tk
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['food-log']
collection = db['gui-log']

window = tk.Tk()

j = 0

for i in collection.find():
    frame = tk.Frame(
        master = window,
    )
    frame.grid(row=j)
    label = tk.Label(
            master=frame,
            text = "Author: "+ i['Author'] + ", Food Eaten: " + i['Food'] + ", Date: " + i['Date'] + ", Calories: " + str(i['Calories']),
            pady=20,
            padx=20
        )
    label.pack()
    j+=1

window.mainloop()
        