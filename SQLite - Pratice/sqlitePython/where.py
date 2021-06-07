import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# Primary key is a uniqe i no
# c.execute("SELECT rowid, * FROM customers WHERE Last_Name = 'Banerjee' ")
# c.execute("SELECT rowid, * FROM customers WHERE age >= 21 ")
c.execute("SELECT rowid, * FROM customers WHERE Last_Name LIKE 'Gu%' ")
# Fetching All the data
items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()  # closing out connection
