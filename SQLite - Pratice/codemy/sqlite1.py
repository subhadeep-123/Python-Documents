import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

c = conn.execute("""CREATE TABLE customers (
                first TEXT,
                last TEXT,
                email text)""")

print("Sucessfully Did what I had to!!")

# Commit our command
conn.commit()

# Close our connection
conn.close()

