import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# Primary key is a uniqe i no
c.execute("SELECT rowid, * FROM customers")

# Fetching All the data
items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()  # closing out connection
