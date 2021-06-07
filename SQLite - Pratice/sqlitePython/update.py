import sqlite3

conn = sqlite3.connect("temp.db")  # This is for db


# Creating a cursor
c = conn.cursor()

# Primary key is a uniqe i no
c.execute("SELECT * FROM customers")

# Fetching All the data
items = c.fetchall()

for item in items:
    print(item)

# Updating a Data
c.execute("""UPDATE customers SET Last_Name = 'Banerjee' 
             WHERE Last_Name LIKE 'Gu%'""")
#  WHERE rowid = 1""")

# Primary key is a uniqe i no
c.execute("SELECT * FROM customers")

# Fetching All the data
items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()  # closing out connection
