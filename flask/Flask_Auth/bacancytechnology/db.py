import sqlite3

con = sqlite3.connect('bookstore.db')
con.commit()
con.close()
