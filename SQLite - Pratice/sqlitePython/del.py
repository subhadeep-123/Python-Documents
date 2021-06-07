import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()


c.execute("DELETE FROM customers WHERE First_Name LIKE 'R%' ")

conn.commit()

c.execute("SELECT * FROM CUSTOMERS")
print(c.fetchall())

conn.commit()

conn.close()  # closing out connection
