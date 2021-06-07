import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# AND _ OR
c.execute(
    "SELECT rowid, * FROM CUSTOMERS WHERE First_Name LIKE 'Su%' AND Email LIKE 'su%' ")
print(c.fetchall())

conn.commit()

conn.close()  # closing out connection
