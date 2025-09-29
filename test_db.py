import database

print("Reservations in DB:")
for row in database.view():
    print(row)

