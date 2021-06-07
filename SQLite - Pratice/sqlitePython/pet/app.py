import database

TABLENAME = 'customers'

# Creating the table
names = database.listTables()
if TABLENAME not in names:
    database.createTable(TABLENAME)
else:
    print(f"SKIPPING - TABLE ALREADY EXISTS - {names} \n")

dataList = [
    ('Sipra Banerjee', 'barnerjeer529@gmail.com', 9831790182, 55),
    ('Subir Banerjee', 'subir20110109@gmail.com', 9831626265, 62),
    ('Swapna Mitra', 'mitraswapna123@gmail.com', 9433851479, 57),
    ('Subhadeep Banerjee', 'subhadeep762@gmail.com', 7980207055, 21)
]
database.insertData(TABLENAME, dataList=dataList)

database.showAll(TABLENAME)

dataList = [
    ('Subhadeep Banerjee', 'subhadeep762@gmail.com', 7980207055, 21),
    ('Ria Gupta', 'riagupta301@gmail.com', 5123456891, 22),
    ('Souma Mitra', 'mitrasouma102@gmail.com', 6444848265, 21),
]
database.insertData(TABLENAME, dataList=dataList)

database.showAll(TABLENAME)

data = ('Ria Gupta', 'riagupta301@gmail.com', 5123456891, 22)
database.deleteOne(TABLENAME, data)

print("\nAfter Deleting\n")
database.showAll(TABLENAME)


database.drop(TABLENAME)
print(f"Remaining Tables - {database.listTables()}")
