import os
import sqlite3
from pprint import pprint

if os.path.isfile('temp.db'):
    os.remove('temp.db')

conn = sqlite3.connect("temp.db")  # This is for db
# conn = sqlite3.connect(":memory:") # This will store the data in mem


# Creating a cursor
c = conn.cursor()


# Datatype in sqlite3
# NULL
# INTEGER
# TEXT
# REAL
# BLOB

# Create a table
c.execute(""" CREATE TABLE customers (
First_Name text,
	Last_Name text,
	Email text,
	PhNo integer
	) """)


# Inserting data to the database, single entry
c.execute("INSERT INTO customers VALUES ('Subhadeep', 'Banerjee', 'subhadeep762@gmail.com', '7980207055')")


# Multiple Entry
customer_list = [
    ('Subir', 'Banerjee', 'subir20110109@gmail.com', '9831626265'),
    ('Sipra', 'Banerjee', 'banerjee6@gmail.com', '9831790182'),
    ('Ria', 'Gupta', 'ria728@gmail.com', '1234567899')
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customer_list)

print("Data Inserted")


# Fetching All the data
c.execute("SELECT * FROM customers")
# print("Fetching All\n")
# pprint(c.fetchall(), indent=4)

# print("Fetching One")
# pprint(c.fetchone())

# print("Fetching Two")
# pprint(c.fetchmany(2), indent=4)

# print("Fetching One Using Indexing")
# pprint(c.fetchone()[0])

# Iterating over fetch all
for i in c.fetchall():
    print(i[0])
# commit out connection. for executing the obove connections
conn.commit()

# closing out connection
conn.close()
