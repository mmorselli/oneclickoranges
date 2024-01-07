import tkinter as tk
import json

def config_form(frame):
    # Create text entry fields
    entries = []
    for i in range(4):
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1)
        entries.append(entry)

    # Create save button
    def save_data():
        data = [entry.get() for entry in entries]
        with open('config.json', 'w') as f:
            json.dump(data, f)

    save_button = tk.Button(frame, text="SAVE", command=save_data)
    save_button.grid(row=5, column=1)

