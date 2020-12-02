import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# c.execute("SELECT * FROM customers WHERE last = 'Banerjee' ")
# we can use > < >= <= != ==
# c.execute("SELECT * FROM customers WHERE last LIKE 'Ba%' ")

c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com' ")
items = c.fetchall()

# print(items)

#or

#since it is a tuple we can do tuplee things to it!!
for item in items:
    print(item)
conn.commit()

conn.close()