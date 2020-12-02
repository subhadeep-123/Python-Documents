import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

customer_list = [
    ('Subhadeep', 'Banerjee', 'subhadeep762@gmail.com'),
    ('Richard', 'Chakraborty', 'flip.brian35@gmail.com'),
    ('Soumya', 'Mitra', 'soumyamitra99@gmail.com'),
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", customer_list)

conn.commit()
conn.close()