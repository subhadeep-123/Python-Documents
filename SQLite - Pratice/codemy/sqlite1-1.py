import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("INSERT INTO customers VALUES ('Subhadeep', 'Banerjee', 'subhadeep@klizos.com')")
c.execute("INSERT INTO customers VALUES ('Subhadeep', 'Banerjee', 'subhadeep@klizos.com')")

print('Succesfully Executed!!')
conn.commit()

conn.close()