import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# AND _ OR _ LIMIT
c.execute(
    "SELECT rowid, * FROM CUSTOMERS WHERE First_Name LIKE 'Su%' AND Email LIKE 'su%' LIMIT 1")
print(c.fetchall())

conn.commit()

conn.close()  # closing out connection
