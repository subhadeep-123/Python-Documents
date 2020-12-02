# Order By Record
import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT  rowid, * FROM customers ORDER BY rowid ASC")
c.execute("SELECT  rowid, * FROM customers ORDER BY rowid DESC")
c.execute("SELECT  rowid, * FROM customers ORDER BY last")
c.execute("SELECT  rowid, * FROM customers ORDER BY last DESC")
items = c.fetchall()
for item in items:
    print(item)
conn.commit()

conn.close()
