# Update Record
import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# c.execute("""UPDATE customers SET first = 'Chandrabali' WHERE email LIKE '%762@gmail.com' """)
#Changnig by rowid
c.execute("""UPDATE customers SET first = 'Chandrabali', email = 'chandrabali@gmail.com' WHERE rowid = 2""")

conn.commit()

c.execute("SELECT  rowid, * FROM customers")
items = c.fetchall()
#since it is a tuple we can do tuplee things to it!!
for item in items:
    print(item)
conn.commit()

conn.close()
