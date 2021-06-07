import sqlite3


def createTable(tablename):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute(f"""CREATE TABLE {tablename} (
        name text,
        email text,
        ph integer,
        age integer
    )""")
    conn.commit()
    conn.close()


def listTables():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != 'sqlite_sequence'
    ]
    cursor.close()
    return tables


def insertData(tablename, dataList):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    for i in dataList:
        c.execute(f"SELECT * FROM {tablename} WHERE ph={str(i[2])}")
        result = c.fetchone()
        if result:
            print(f"SKIPPING INSERT FOR - {i}")
        else:
            print(f"INSERTING - {i}")
            c.execute(f"INSERT INTO {tablename} VALUES (?, ?, ?, ?)", i)
    else:
        print("All Data Inserted")
    conn.commit()
    conn.close()


def deleteOne(tablename, data):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute(
        f"DELETE FROM {tablename} WHERE ph = {data[2]}")
    print(f"Item Deleted - {data}")
    conn.commit()
    conn.close()


def showAll(tablename):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM {tablename}")
    for item in c.fetchall():
        print(item)
    conn.commit()
    conn.close()

def drop(tablename):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute(f"DROP TABLE {tablename}")
    conn.commit()
    conn.close()
if __name__ == '__main__':
    pass
