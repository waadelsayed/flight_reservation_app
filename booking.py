import tkinter as tk
from tkinter import messagebox
from database import insert

def show_booking(root, go_home):
    # Clear current page
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Book a Flight")

    # Define fields
    fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    entries = {}

    # Create form
    for i, field in enumerate(fields):
        tk.Label(root, text=field, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(root, width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field.lower().replace(" ", "_")] = entry  # Store entry widget

    # Submit button
    def submit():
        values = [entry.get().strip() for entry in entries.values()]
        if all(values):
            insert(*values)
            messagebox.showinfo("Success", "Flight booked successfully!")
            go_home()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # Buttons
    tk.Button(root, text="Submit", command=submit, width=20).grid(row=len(fields), column=0, columnspan=2,pady=20)
    tk.Button(root, text="Back", command=go_home).grid(row=len(fields)+1, column=0, columnspan=2)
