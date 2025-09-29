import tkinter as tk

def show_home(root, show_booking, show_reservations):
    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Flight Reservation - Home")

    # Title
    tk.Label(root, text="Flight Reservation System", font=("Arial", 20)).pack(pady=30)

    # Book Flight Button
    tk.Button(
        root,
        text="Book Flight",
        font=("Arial", 14),
        width=20,
        command=show_booking
    ).pack(pady=10)

    # View Reservations Button
    tk.Button(
        root,
        text="View Reservations",
        font=("Arial", 14),
        width=20,
        command=show_reservations
    ).pack(pady=10)
