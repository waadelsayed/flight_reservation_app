import tkinter as tk
from database import connect
from home import show_home
from booking import show_booking
from reservations import show_reservations

def main():
    connect()  # Ensure database and table exist

    root = tk.Tk()
    root.geometry("500x400")  # Set window size
    root.title("Flight Reservation App")

    # Navigation functions
    def go_home():
        show_home(root, go_booking, go_reservations)

    def go_booking():
        show_booking(root, go_home)

    def go_reservations():
        show_reservations(root, go_home)

    # Start on the home page
    go_home()

    root.mainloop()

if __name__ == "__main__":
    main()
