import tkinter as tk
from tkinter import messagebox
from database import update

def show_edit_reservation(root, go_home, reservation):
    # Clear current page
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Edit Reservation")

    reservation_id = reservation[0]  # أول عنصر هو الـ ID

    # Labels and entry fields
    labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(root, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(root, width=30)
        entry.insert(0, reservation[i+1])  # نبدأ من index 1 (لأن index 0 هو ID)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    # Update button
    def save_update():
        new_values = [e.get() for e in entries]
        update(reservation_id, *new_values)
        messagebox.showinfo("Updated", "Reservation updated successfully!")
        go_home()  # رجّعنا للهوم أو صفحة عرض الحجوزات

    tk.Button(root, text="Update", command=save_update).grid(row=len(labels), column=0, pady=20)
    tk.Button(root, text="Back", command=go_home).grid(row=len(labels), column=1, pady=20)
