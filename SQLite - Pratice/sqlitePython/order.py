import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# Order By
# desc or aesc
# c.execute("SELECT rowid, * FROM CUSTOMERS ORDER BY rowid desc")
c.execute("SELECT rowid, * FROM CUSTOMERS ORDER BY PhNo desc")
print(c.fetchall())

conn.commit()

conn.close()  # closing out connection
