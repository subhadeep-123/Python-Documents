import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

c.execute("DROP TABLE customers")

c.execute("SELECT rowid, * FROM CUSTOMERS")
print(c.fetchall())

conn.commit()

conn.close()  # closing out connection
