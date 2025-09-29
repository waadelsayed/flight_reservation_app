import tkinter as tk
from tkinter import messagebox
from database import view, delete   # استخدم view بدل fetch
from edit_reservation import show_edit_reservation

def show_reservations(root, go_home):
    # Clear current page
    for widget in root.winfo_children():
        widget.destroy()

    root.title("All Reservations")

    # Heading
    tk.Label(root, text="All Reservations", font=("Arial", 18)).grid(row=0, column=0, columnspan=8, pady=10)

    # Table Header
    headers = ["ID", "Name", "Flight", "From", "To", "Date", "Seat", "Actions"]
    for col, header in enumerate(headers):
        tk.Label(
            root, text=header, font=("Arial", 10, "bold"),
            borderwidth=1, relief="solid", padx=5, pady=5
        ).grid(row=1, column=col, sticky="nsew")

    # Fetch and display reservations
    rows = view()
    for i, row in enumerate(rows, start=2):  # Start from row 2 (after header)
        for j, value in enumerate(row):
            tk.Label(
                root, text=value,
                borderwidth=1, relief="solid", padx=5, pady=5
            ).grid(row=i, column=j, sticky="nsew")

        # Edit button
        tk.Button(
            root, text="Edit",
            command=lambda r=row: show_edit_reservation(root, go_home, r)
        ).grid(row=i, column=len(headers)-1, sticky="w", padx=2)

        # Delete button
        tk.Button(
            root, text="Delete",
            command=lambda id=row[0]: confirm_delete(root, id, go_home)
        ).grid(row=i, column=len(headers)-1, sticky="e", padx=2)

    # Back Button (use grid instead of pack)
    tk.Button(root, text="Back", command=go_home).grid(row=len(rows)+2, column=0, columnspan=8, pady=20)


def confirm_delete(root, id, go_home):
    answer = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
    if answer:
        delete(id)
        messagebox.showinfo("Deleted", "Reservation deleted.")
        show_reservations(root, go_home)  # Refresh the list
