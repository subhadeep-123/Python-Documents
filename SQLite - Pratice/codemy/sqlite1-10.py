# And / Or
import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT  rowid, * FROM customers WHERE last LIKE 'B%' AND rowid=1")
c.execute("SELECT  rowid, * FROM customers WHERE last LIKE 'B%' OR rowid=1")

items = c.fetchall()
for item in items:
    print(item)
conn.commit()

conn.close()
