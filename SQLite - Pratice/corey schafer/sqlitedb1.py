import sqlite3
from database1 import Employee

# for in memory databsae
conn = sqlite3.connect(':memory:')
# Since it stays in the ram it is good for testing 
# meaning when we want a new database everytinm

# To establish connection
# conn = sqlite3.connect('database1.db')

#For Curson
c = conn.cursor()

# In SQLite we have mainly 5 datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

#To execute a SQL command
c.execute('''CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )
        ''')

#add data to the database
# c.execute("INSERT INTO employees VALUES ('Subhadeep', 'Banerjee', 1000000)")
# c.execute("INSERT INTO employees VALUES ('Richard', 'Chakborty', 500000)")


# #Select a data and also it provides some result where we can iterate through
# c.execute("SELECT * FROM employees WHERE last='Gupta'")
# print(c.fetchone())

emp_1 = Employee('Subhadeep', 'Banerjee', 999999999)
emp_2 = Employee('Richard', 'Chakborty', 99999999)
emp_3 = Employee('Soumya', 'Mitra', 99999999)

#format string literal are vulnerable to sql injection
#first way
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, 
#                                                     emp_1.last, 
#                                                     emp_1.pay))
#second way
for i in [emp_1, emp_2, emp_3]:
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': i.first, 
                                                                'last': i.last, 
                                                                'pay': i.pay}) 

# #Select a data and also it provides some result where we can iterate through
c.execute("SELECT * FROM employees WHERE last=?", ('Banerjee', ))
print(c.fetchone())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Mitra'})
print(c.fetchone())

# This commits the currennt transaction
conn.commit()

# To close the connection with the database
conn.close()