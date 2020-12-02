import sqlite3
import pprint

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")

pprint.pprint(c.fetchall())

print(c.fetchone())
print(c.fetchone()[0])

print(c.fetchmany(2))
#Every time we fetch the coursor changes it loc same as file
#I wonder if we have seek here

conn.commit()

conn.close()