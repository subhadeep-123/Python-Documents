#primary Key Conpect

import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)
conn.commit()

conn.close()