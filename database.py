import sqlite3

# Create the database and reservations table
def connect():
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insert new reservation
def insert(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO reservations VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

# Get all reservations (renamed from fetch → view)
def view():
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    conn.close()
    return rows

# Update a reservation
def update(id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE reservations SET 
            name = ?, 
            flight_number = ?, 
            departure = ?, 
            destination = ?, 
            date = ?, 
            seat_number = ?
        WHERE id = ?
    """, (name, flight_number, departure, destination, date, seat_number, id))
    conn.commit()
    conn.close()

# Delete a reservation
def delete(id):
    conn = sqlite3.connect("flights.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id = ?", (id,))
    conn.commit()
    conn.close()
