import sqlite3
from database1 import Employee

# for in memory databsae
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('test.db')

#For Curson
c = conn.cursor()

#To execute a SQL command
c.execute('''CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )
        ''')

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 
                                                                        'last': emp.last, 
                                                                        'pay': emp.pay}) 

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
                     WHERE first = :first AND last = :last""",
                     {"first": emp.first,
                      "last": emp.last,
                      "pay": pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 
                   'last': emp.last})


emp_1 = Employee('Subhadeep', 'Banerjee', 999999999)
emp_2 = Employee('Richard', 'Chakborty', 99999999)
emp_3 = Employee('Soumya', 'Mitra', 99999999)
emp_4 = Employee('Shubham', 'Nag', 500000)
emp_5 = Employee('Suvhradip', 'Ghosh', 20000)
emp_6 = Employee('Ayan', 'Ghosh', 100)
emp_7 = Employee('Chandrabali', 'Banerjee', 99999999)
emp_8 = Employee('Sneha', 'Banerjee', 100)
emp_9 = Employee('Rajarshee', 'Bhadra', 500)
emp_10 = Employee('Litisha', 'Mahapatro', 200)
emp_11 = Employee('Shreya', 'Mukherjee', 9999)
emp_12 = Employee('Sweta', 'Kar', 5000)
emp_13 = Employee('Satej', 'Manna', 5000)

#inserting to the database
for i in range(1, 14):
    eval(f'insert_emp(emp_{i})')

emps = get_emps_by_name('Banerjee')
print(emps)

update_pay(emp_4, 100)
remove_emp(emp_8)

emps = get_emps_by_name('Banerjee')
print(emps)

# To close the connection with the database
conn.close() 